"""Node 6 — Next Actions. Appends deeplinks and dynamic follow-up prompts."""
from src.agent.state import AgentState, NextAction


def build_next_actions(state: AgentState) -> dict:
    # Phase 6 will implement intent-aware CTA generation.
    actions: list[NextAction] = []
    return {"next_actions": actions}
