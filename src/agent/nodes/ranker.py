"""Node 4 — Ranker. Scores results by trust, relevance, and recency."""
from src.agent.state import AgentState, RankedResult


def rank_results(state: AgentState) -> dict:
    # Phase 5 will implement scoring logic.
    ranked: list[RankedResult] = [
        {**r, "score": 1.0} for r in state["valid_results"]  # type: ignore[misc]
    ]
    return {"ranked_results": ranked}
