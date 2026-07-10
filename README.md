# Veritas
# Project Structure

```text
Veritas/
│
├── README.md                 # Documentation
├── LICENSE                   # License
├── .gitignore                # Git rules
├── .env.example              # Env template
├── requirements.txt          # Dependencies
├── docker-compose.yml        # Docker setup
├── Dockerfile                # Container
│
├── app/                      # Application
│   ├── api/                  # Endpoints
│   ├── agents/               # AI Agents
│   ├── orchestrator/         # Workflow
│   ├── retrieval/            # RAG Engine
│   ├── sources/              # Data Sources
│   ├── llm/                  # LLM Logic
│   ├── memory/               # Memory
│   ├── evaluation/           # Validation
│   ├── schemas/              # Models
│   ├── services/             # Services
│   ├── utils/                # Utilities
│   ├── config.py             # Config
│   └── main.py               # Entry Point
│
├── data/                     # Storage
│   ├── raw/                  # Raw Data
│   ├── processed/            # Clean Data
│   ├── embeddings/           # Vectors
│   └── cache/                # Cache
│
├── notebooks/                # Experiments
├── tests/                    # Unit Tests
├── scripts/                  # Automation
├── docs/                     # Documentation
└── .github/                  # CI/CD
    └── workflows/            # GitHub Actions
```
