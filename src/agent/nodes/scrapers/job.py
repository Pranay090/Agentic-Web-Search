"""Node 2A — Job scraper. Targets LinkedIn / Indeed / Glassdoor via search."""
from src.agent.state import AgentState, RawResult


def scrape_jobs(state: AgentState) -> dict:
    # Phase 3 will implement Tavily + targeted job-board crawl.
    raw: list[RawResult] = []
    return {"raw_results": raw}
