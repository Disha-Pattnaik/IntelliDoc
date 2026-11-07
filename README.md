# IntelliDoc – AI-Powered Document Assistant

IntelliDoc is an AI-powered document assistant that allows users to upload PDF documents, ask questions, generate summaries, and prepare interview questions using Generative AI and Retrieval-Augmented Generation (RAG).

## Features

- **PDF Processing:** Extracts text from uploaded PDF documents.
- **Text Chunking:** Divides extracted text into smaller overlapping chunks.
- **Semantic Embeddings:** Uses Sentence Transformers to convert text into numerical vectors.
- **Vector Search:** Uses FAISS to retrieve relevant document chunks.
- **RAG-Based Question Answering:** Uses retrieved document context to generate answers with Gemini.
- **Document Summarisation:** Generates concise document summaries.
- **Interview Question Generator:** Creates technical questions and answers from uploaded documents.
- **AI Agent:** Implements Gemini function calling to select document-related tools.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM | Google Gemini |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | FAISS |
| PDF Processing | PyPDF |
| Testing | Pytest |
| Environment Management | Python Virtual Environment |

## Project Architecture

1. User uploads a PDF document.
2. PyPDF extracts its text.
3. The extracted text is divided into overlapping chunks.
4. Sentence Transformers generates embeddings.
5. FAISS stores the embeddings and performs similarity search.
6. When a user asks a question, relevant chunks are retrieved.
7. Gemini generates an answer using the retrieved context.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd IntelliDoc
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### 6. Run the application

```bash
streamlit run app.py
```

## Running Tests

Execute the unit tests using:

```bash
pytest -v
```

The project currently includes tests for PDF text chunking and FAISS vector search.

## Future Improvements

- Add more comprehensive automated tests.
- Improve document processing and retrieval accuracy.
- Add support for multiple document formats.
- Implement persistent vector storage.
- Docker-based deployment.
- Improve AI agent validation and tool execution.