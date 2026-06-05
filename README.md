# Aiden AI — Intelligent Web Crawler & Answer Agent

> Hackathon submission for Problem Statement 5.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# fill in ANTHROPIC_API_KEY and TAVILY_API_KEY
```

## Run

```bash
PYTHONPATH=. streamlit run src/ui/app.py
```

## Architecture

See [docs/architecture.md](docs/architecture.md).

## Project Structure

```
src/
├── agent/
│   ├── state.py          # Shared AgentState TypedDict
│   ├── graph.py          # LangGraph pipeline (all nodes wired)
│   └── nodes/
│       ├── intent.py     # Node 1 — Intent classifier
│       ├── scrapers/
│       │   ├── job.py    # Node 2A — Job scraper
│       │   ├── product.py # Node 2B — Product scraper
│       │   └── general.py # Node 2C — General scraper
│       ├── validator.py  # Node 3 — Scam / 404 filter
│       ├── ranker.py     # Node 4 — Relevance ranker
│       ├── extractor.py  # Node 5 — Extractor & summarizer
│       └── next_actions.py # Node 6 — CTA / deeplinks
└── ui/
    └── app.py            # Streamlit chat UI
```
