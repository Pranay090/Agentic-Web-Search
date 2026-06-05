"""Node 1 — Intent classifier. Routes query to job / product / general."""
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate

from src.agent.llm import llm
from src.agent.state import AgentState


class IntentOutput(BaseModel):
    intent: str  # "job" | "product" | "general"
    reasoning: str


_SYSTEM = """You are an intent classifier for a web-search agent.
Classify the user's query into exactly ONE of these categories:

- job      : looking for jobs, internships, roles, hiring, employment
- product  : looking to buy something, best-of lists, product reviews, pricing comparisons
- general  : everything else (news, how-to guides, factual Q&A, research)

Respond with the intent and a one-sentence reasoning."""

_prompt = ChatPromptTemplate.from_messages([
    ("system", _SYSTEM),
    ("human", "{query}"),
])

_chain = _prompt | llm.with_structured_output(IntentOutput)


def classify_intent(state: AgentState) -> dict:
    query = state["query"]
    result: IntentOutput = _chain.invoke({"query": query})
    print(f"[Intent] '{query}' → {result.intent}  ({result.reasoning})")
    return {"intent": result.intent}
