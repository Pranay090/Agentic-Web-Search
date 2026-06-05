"""Node 2C — General scraper. Targets Google / Bing via Tavily search API."""
from src.agent.state import AgentState, RawResult


def scrape_general(state: AgentState) -> dict:
    # Phase 3 will implement Tavily search.
    raw: list[RawResult] = []
    return {"raw_results": raw}
