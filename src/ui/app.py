"""Streamlit Chat UI — Phase 7 will fully style this."""
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from src.agent.graph import graph
from src.agent.state import AgentState

st.set_page_config(page_title="Aiden AI", page_icon="🔍", layout="centered")
st.title("🔍 Aiden AI — Intelligent Web Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me anything — jobs, products, or general questions…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching the web…"):
            initial_state: AgentState = {
                "messages": [{"role": "user", "content": prompt}],
                "query": prompt,
                "intent": "",
                "raw_results": [],
                "valid_results": [],
                "ranked_results": [],
                "summary_cards": [],
                "next_actions": [],
                "answer": "",
            }
            result = graph.invoke(initial_state)

        answer = result.get("answer", "No answer generated.")
        st.markdown(answer)

        # Show next-action buttons (Phase 6+)
        for action in result.get("next_actions", []):
            st.link_button(action["label"], action["url"])

    st.session_state.messages.append({"role": "assistant", "content": answer})
