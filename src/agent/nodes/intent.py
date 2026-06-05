"""Node 1 — Intent classifier. Routes query to job / product / general."""
from src.agent.state import AgentState


def classify_intent(state: AgentState) -> dict:
    # Phase 2 will implement LLM classification.
    # Stub: always routes to general.
    return {"intent": "general"}
