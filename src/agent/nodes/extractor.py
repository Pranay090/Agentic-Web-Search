"""Node 5 — Extractor & Summarizer. Generates clean markdown cards via LLM."""
from src.agent.state import AgentState, SummaryCard


def extract_and_summarize(state: AgentState) -> dict:
    # Phase 5 will implement LLM-powered extraction + markdown card generation.
    cards: list[SummaryCard] = []
    answer = "*(no results yet — scrapers not yet implemented)*"
    return {"summary_cards": cards, "answer": answer}
