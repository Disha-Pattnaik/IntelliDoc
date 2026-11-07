from google import genai
from google.genai import types

from config import GEMINI_API_KEY

from embedding_service import generate_embeddings

from vector_store import search_similar_chunks

from gemini_service import (
    generate_summary,
    generate_interview_questions as create_questions
)


# INITIALISE GEMINI CLIENT

client = genai.Client(api_key=GEMINI_API_KEY)


# CREATE AI AGENT

def run_agent(user_request, document_text, chunks, index):

    # TOOL 1: DOCUMENT SEARCH
    def search_document(query: str) -> str:
        """Search the uploaded PDF for information relevant to a query."""

        query_embedding = generate_embeddings([query])

        results = search_similar_chunks(
            index,
            query_embedding,
            chunks,
            top_k=3
        )

        return "\n\n".join(
            result["chunk"] for result in results
        )

    # TOOL 2: DOCUMENT SUMMARISATION
    def summarize_document() -> str:
        """Generate a summary of the uploaded PDF."""

        return generate_summary(document_text)

    # TOOL 3: INTERVIEW QUESTION GENERATION
    def generate_questions() -> str:
        """Generate technical interview questions and answers from the PDF."""

        return create_questions(document_text)

    # SEND REQUEST TO GEMINI AGENT

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=user_request,
        config=types.GenerateContentConfig(
            tools=[
                search_document,
                summarize_document,
                generate_questions
            ],
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                maximum_remote_calls=4
            )
        )
    )

    return response.text