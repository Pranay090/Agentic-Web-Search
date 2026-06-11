"""Shared Tavily search client and helper."""
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])


def tavily_search(
    query: str,
    max_results: int = 7,
    include_domains: list[str] | None = None,
    days: int | None = None,
) -> list[dict]:
    """Returns raw Tavily result dicts: {url, title, content, score}.
    Falls back to basic search depth if advanced times out.
    """
    kwargs: dict = {
        "query": query,
        "max_results": max_results,
        "include_raw_content": False,
    }
    if include_domains:
        kwargs["include_domains"] = include_domains
    if days:
        kwargs["days"] = days

    # Try advanced first (richer results), fall back to basic on timeout
    for depth in ("advanced", "basic"):
        try:
            response = _client.search(**kwargs, search_depth=depth)
            return response.get("results", [])
        except Exception as e:
            print(f"[Tavily] {depth} search failed: {e}. {'Retrying with basic...' if depth == 'advanced' else 'Returning empty.'}")

    return []
