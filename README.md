# Veritas
# 📂 Project Structure

```text
Veritas/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── dependencies.py
│   │
│   ├── api/
│   │   ├── routes.py
│   │   ├── research.py
│   │   └── health.py
│   │
│   ├── orchestrator/
│   │   ├── planner.py
│   │   ├── executor.py
│   │   ├── workflow.py
│   │   └── state.py
│   │
│   ├── agents/
│   │   ├── retrieval_agent.py
│   │   ├── extraction_agent.py
│   │   ├── verification_agent.py
│   │   ├── reasoning_agent.py
│   │   ├── citation_agent.py
│   │   └── report_agent.py
│   │
│   ├── retrieval/
│   │   ├── vectorstore.py
│   │   ├── embeddings.py
│   │   ├── bm25.py
│   │   ├── reranker.py
│   │   └── hybrid_search.py
│   │
│   ├── sources/
│   │   ├── arxiv.py
│   │   ├── pubmed.py
│   │   ├── news.py
│   │   ├── wikipedia.py
│   │   └── web_search.py
│   │
│   ├── llm/
│   │   ├── models.py
│   │   ├── prompts.py
│   │   ├── parser.py
│   │   └── response_formatter.py
│   │
│   ├── memory/
│   │   ├── redis_store.py
│   │   ├── cache.py
│   │   └── conversation.py
│   │
│   ├── evaluation/
│   │   ├── hallucination.py
│   │   ├── factual_score.py
│   │   ├── confidence.py
│   │   └── metrics.py
│   │
│   ├── schemas/
│   │   ├── request.py
│   │   ├── response.py
│   │   └── citation.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   ├── helpers.py
│   │   ├── tokenizer.py
│   │   └── exceptions.py
│   │
│   └── services/
│       ├── embedding_service.py
│       ├── llm_service.py
│       └── retrieval_service.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── embeddings/
│   └── cache/
│
├── notebooks/
│   ├── retrieval_testing.ipynb
│   ├── reranking.ipynb
│   └── experiments.ipynb
│
├── tests/
│   ├── test_api.py
│   ├── test_agents.py
│   ├── test_retrieval.py
│   ├── test_orchestrator.py
│   └── test_verification.py
│
├── scripts/
│   ├── build_index.py
│   ├── ingest_data.py
│   ├── evaluate.py
│   └── populate_vector_db.py
│
├── docs/
│   ├── architecture.md
│   ├── api.md
│   ├── setup.md
│   └── roadmap.md
│
└── .github/
    └── workflows/
        ├── tests.yml
        └── lint.yml
```
