# IntelliDoc – AI-Powered Document Assistant

## Live Demo

Try IntelliDoc here:

🚀 [Launch IntelliDoc](https://my-intellidoc.streamlit.app/)

Upload a PDF and explore document question answering, summarisation and interview question generation.

The project combines Large Language Models (LLMs), semantic search, vector embeddings, and AI-powered tool calling to provide an interactive document analysis experience.

## Features

- **PDF Processing:** Extracts text from uploaded PDF documents using PyPDF.
- **Text Chunking:** Divides extracted text into smaller, overlapping chunks for efficient retrieval.
- **Semantic Embeddings:** Uses Sentence Transformers to convert text into numerical vector representations.
- **Vector Search:** Uses FAISS to store embeddings and retrieve relevant document chunks through similarity search.
- **RAG-Based Question Answering:** Retrieves relevant document context and uses Google Gemini to generate context-aware answers.
- **Document Summarisation:** Generates concise and structured summaries of uploaded documents.
- **Interview Question Generator:** Creates basic, intermediate, and advanced technical questions with answers based on document content.
- **Agentic AI Assistant:** Integrates Gemini function calling to select and execute document-related tools, including document search, summarisation, and interview question generation.
- **Interactive Interface:** Provides an easy-to-use web interface built with Streamlit.
- **Automated Testing:** Uses Pytest to test PDF processing and FAISS vector search functionality.
- **Docker Support:** Containerises the application for consistent execution across environments.
- **CI/CD Automation:** Uses GitHub Actions to automatically execute unit tests and build Docker images when code is pushed or pull requests are created.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python 3.11 |
| Frontend | Streamlit |
| LLM | Google Gemini |
| LLM Integration | Google Gen AI SDK |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | FAISS |
| PDF Processing | PyPDF |
| Testing | Pytest |
| Environment Management | Python Virtual Environment |
| Containerisation | Docker |
| CI/CD | GitHub Actions |
| Version Control | Git and GitHub |
| Cloud Deployment | Streamlit Community Cloud |

## Project Architecture

### 1. Document Processing and RAG Workflow

1. The user uploads a PDF document through the Streamlit interface.
2. PyPDF extracts text from the uploaded document.
3. The extracted text is divided into smaller overlapping chunks.
4. Sentence Transformers generates 384-dimensional embeddings for the text chunks.
5. FAISS stores the embeddings in a vector index.
6. When the user submits a question, the question is converted into an embedding using the same embedding model.
7. FAISS performs similarity search and retrieves the most relevant document chunks.
8. The retrieved context and user question are passed to Google Gemini.
9. Gemini generates an answer grounded in the retrieved document content.

### 2. Agentic AI Workflow

The AI Agent uses Gemini function calling to select appropriate tools based on the user's request.

Available tools:

- **Document Search:** Retrieves relevant information from the uploaded PDF using semantic search.
- **Document Summarisation:** Generates a summary of the uploaded document.
- **Interview Question Generation:** Generates technical interview questions and answers from the document.

The agent analyses the user's request and determines which tool or tools are appropriate for completing the task.

**Validation note:** Agentic AI function calling has been implemented. Full end-to-end validation is pending due to Gemini API availability limitations.

## Project Structure

```text
IntelliDoc/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── docker.yml
│
├── tests/
│   ├── test_pdf_processor.py
│   └── test_vector_store.py
│
├── app.py
├── agent_service.py
├── config.py
├── embedding_service.py
├── gemini_service.py
├── pdf_processor.py
├── vector_store.py
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
└── .env
```

**Note:** The `.env` file contains the Gemini API key and is excluded from version control through `.gitignore`. It should be created locally and must never be committed to GitHub.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Disha-Pattnaik/IntelliDoc.git
cd IntelliDoc
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own Gemini API key.

### 6. Run the application

```bash
streamlit run app.py
```

Open the local Streamlit URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## Running Tests

Execute the automated unit tests using:

```bash
pytest -v tests/
```

The current test suite covers:

- PDF text extraction and chunking.
- Chunk size and overlap validation.
- Invalid input handling.
- FAISS vector index creation.
- Similarity search and distance calculation.
- Empty vector store handling.

**Test Results: 17 tests passed successfully.**

These are unit tests for PDF processing and vector search. Gemini integration and complete Agentic AI workflows are not covered by the current test suite.

## Docker Setup and Execution

IntelliDoc supports Docker containerisation to provide a consistent application environment.

### 1. Prerequisites

- Docker Desktop installed.
- Docker Engine running.

### 2. Build the Docker image

Run the following command from the project root:

```bash
docker build -t intellidoc .
```

This builds the application image using the project Dockerfile.

The Docker configuration uses CPU-only PyTorch installation to reduce unnecessary