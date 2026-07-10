# Veritas
```text
veritas/
│
├── frontend/                     # React + Vite Frontend
│   ├── src/
│   │   ├── components/           # UI Components
│   │   ├── pages/                # Application Pages
│   │   ├── services/             # API Calls
│   │   ├── hooks/                # Custom Hooks
│   │   ├── assets/               # Images & Icons
│   │   ├── styles/               # CSS Files
│   │   ├── App.jsx               # Root Component
│   │   └── main.jsx              # Entry Point
│   ├── public/                   # Static Files
│   ├── package.json              # Dependencies
│   └── vite.config.js            # Vite Config
│
├── backend/                      # FastAPI Backend
│   ├── routes/                   # API Endpoints
│   ├── middleware/               # Middleware
│   ├── database/                 # Database Logic
│   ├── services/                 # Backend Services
│   ├── models/                   # Pydantic Models
│   ├── utils/                    # Utilities
│   ├── config.py                 # Configuration
│   ├── main.py                   # FastAPI Entry
│   └── requirements.txt          # Python Dependencies
│
├── ai/                           # AI Engine
│   ├── agents/                   # AI Agents
│   ├── retrieval/                # RAG Pipeline
│   ├── llm/                      # LLM Wrapper
│   ├── prompts/                  # Prompt Templates
│   ├── memory/                   # Conversation Memory
│   ├── evaluation/               # Fact Verification
│   ├── embeddings/               # Embedding Models
│   ├── sources/                  # arXiv, PubMed, News APIs
│   └── orchestrator/             # Agent Coordinator
│
├── data/                         # Local Data
│   ├── raw/                      # Raw Documents
│   ├── processed/                # Processed Data
│   ├── embeddings/               # Vector Store
│   └── cache/                    # Cached Results
│
├── docs/                         # Documentation
├── tests/                        # Test Suite
├── scripts/                      # Automation Scripts
│
├── .env.example                  # Environment Variables
├── .gitignore                    # Git Ignore Rules
├── Dockerfile                    # Docker Config
├── docker-compose.yml            # Multi-container Setup
├── requirements.txt              # Global Dependencies
├── LICENSE                       # License
└── README.md                     # Project Documentation
```
