"""Node 2B — Product scraper. Targets review sites and commerce engines."""
from src.agent.state import AgentState, RawResult


def scrape_products(state: AgentState) -> dict:
    # Phase 3 will implement Tavily + targeted product-review crawl.
    raw: list[RawResult] = []
    return {"raw_results": raw}
