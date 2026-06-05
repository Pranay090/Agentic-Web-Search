"""Node 3 — Validator. Filters 404s, scam patterns, and spambots."""
from src.agent.state import AgentState, RawResult


def validate_results(state: AgentState) -> dict:
    # Phase 4 will implement HTTP HEAD checks + heuristic scam filter.
    valid: list[RawResult] = state["raw_results"]
    return {"valid_results": valid}
