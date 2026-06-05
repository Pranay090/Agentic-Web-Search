"""LangGraph graph definition — wires all nodes into the pipeline."""
from langgraph.graph import StateGraph, END

from src.agent.state import AgentState
from src.agent.nodes.intent import classify_intent
from src.agent.nodes.scrapers.job import scrape_jobs
from src.agent.nodes.scrapers.product import scrape_products
from src.agent.nodes.scrapers.general import scrape_general
from src.agent.nodes.validator import validate_results
from src.agent.nodes.ranker import rank_results
from src.agent.nodes.extractor import extract_and_summarize
from src.agent.nodes.next_actions import build_next_actions


def _route_by_intent(state: AgentState) -> str:
    """Conditional edge: routes to the appropriate scraper node."""
    intent = state.get("intent", "general")
    if intent == "job":
        return "scrape_jobs"
    if intent == "product":
        return "scrape_products"
    return "scrape_general"


def build_graph() -> StateGraph:
    g = StateGraph(AgentState)

    # Nodes
    g.add_node("classify_intent", classify_intent)
    g.add_node("scrape_jobs", scrape_jobs)
    g.add_node("scrape_products", scrape_products)
    g.add_node("scrape_general", scrape_general)
    g.add_node("validate_results", validate_results)
    g.add_node("rank_results", rank_results)
    g.add_node("extract_and_summarize", extract_and_summarize)
    g.add_node("build_next_actions", build_next_actions)

    # Edges
    g.set_entry_point("classify_intent")

    g.add_conditional_edges(
        "classify_intent",
        _route_by_intent,
        {
            "scrape_jobs": "scrape_jobs",
            "scrape_products": "scrape_products",
            "scrape_general": "scrape_general",
        },
    )

    for scraper in ("scrape_jobs", "scrape_products", "scrape_general"):
        g.add_edge(scraper, "validate_results")

    g.add_edge("validate_results", "rank_results")
    g.add_edge("rank_results", "extract_and_summarize")
    g.add_edge("extract_and_summarize", "build_next_actions")
    g.add_edge("build_next_actions", END)

    return g.compile()


# Module-level compiled graph — import this in the UI and tests
graph = build_graph()
