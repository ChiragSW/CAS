# CAS - Codebase Agent

This project is a Retrieval-Augmented Generation (RAG) agent designed to understand and interact with codebases. It ingests external repositories, indexes them using vector embeddings, and allows users to query the codebase using a powerful LLM.

## Table of Contents
- [Tech Stack](#tech-stack-used)
- [Project Structure](#project-structure)
- [How to use?](#how-to-use)

## Tech Stack used
| Stack | Tech |
|----------|----------|
| Language | ![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white) |
| Frameworks | ![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white) ![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?logo=langchain&logoColor=white) |
| AI / ML | ![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?logo=google&logoColor=white) ![Sentence Transformers](https://img.shields.io/badge/Sentence%20Transformers-FF6F00?logo=huggingface&logoColor=white) |
| Database | ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6F00?logo=chroma&logoColor=white) |
| Utilities | ![PyPDF](https://img.shields.io/badge/PyPDF-3776AB?logo=python&logoColor=white) ![PyMuPDF](https://img.shields.io/badge/PyMuPDF-3776AB?logo=python&logoColor=white) |

## Project Structure
```
RAG/
│
├── add_repo.py                     # Script to ingest external repositories
├── run_app.bat                     # Batch script to run the application
├── requirements.txt                # Project dependencies
├── .env                            # Environment variables (API keys)
│
├── intern/                         # Core internal logic
│   ├── agent/                      # Agent definition
│   │   ├── graph.py                # LangGraph workflow definition
│   │   ├── state.py                # Agent state definition
│   │   └── tools.py                # Custom tools for the agent
│   │
│   ├── app/                        # FastAPI application
│   │   └── main.py                 # API entry point
│   │
│   ├── db/                         # Database handling
│   │
│   └── ingest/                     # Ingestion logic
│       └── ingest_codebase.py      # Logic to ingest code into ChromaDB
│
├── source_code/                    # Directory where ingested repos are stored
│   └── ...
│
├── testfiles/                      # Files for testing
│
└── venv/                           # Virtual environment
```

## How to use?

### 1. Setup Environment
Ensure you have Python installed. Create a virtual environment and install dependencies.

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the root directory and add your Google API key:
```env
GOOGLE_API_KEY=your_api_key_here
```

### 2. Ingest a Repository
To add a codebase for the agent to understand, use the `add_repo.py` script. This will copy the repo to `source_code/` and ingest it into the vector database.

```bash
python add_repo.py /path/to/external/repo
```

### 3. Run the Agent
You can start the FastAPI server using the provided batch script or directly with uvicorn.

**Using Batch Script:**
```bash
run_app.bat
```

**Using Uvicorn:**
```bash
cd intern
uvicorn app.main:app --reload
```

### 4. Query the Agent
Once the server is running (default: `http://localhost:8000`), you can send POST requests to interact with the agent.

**Endpoint:** `POST /`

**Payload:**
```json
{
  "question": "Explain the main logic of the ingested codebase."
}
```

## Author
# Chirag Wattamwar

<p align="center">
  <a href="https://instagram.com/chirag_gg234">
    <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?&logo=instagram&logoColor=white&style=for-the-badge"/>
  </a>
  <a href="https://www.linkedin.com/in/chirag-wattamwar-5b985a313">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
</p>
