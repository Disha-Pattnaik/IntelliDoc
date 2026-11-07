
import time

from google import genai
from config import GEMINI_API_KEY


# ----------------------------------
# STEP 1: INITIALISE GEMINI CLIENT
# ----------------------------------

client = genai.Client(api_key=GEMINI_API_KEY)


# ----------------------------------
# STEP 2: GENERATE RESPONSE
# ----------------------------------

def generate_response(prompt, max_retries=2):

    for attempt in range(max_retries):

        try:

            print("\nSending request to Gemini...")

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            print("Gemini response received successfully!")

            return response.text

        except Exception as e:

            error_message = str(e)

            print("\nGemini API error:", error_message)

            # Handle quota exhaustion
            if (
                "429" in error_message
                or "RESOURCE_EXHAUSTED" in error_message
            ):

                return (
                    "Gemini API quota exhausted. "
                    "Please try again after the quota resets."
                )

            # Handle temporary server timeouts
            elif (
                "504" in error_message
                or "DEADLINE_EXCEEDED" in error_message
            ):

                if attempt < max_retries - 1:

                    print("Temporary server timeout. Retrying...")

                    time.sleep(5)

                else:

                    return (
                        "Gemini server timeout. "
                        "Please try again later."
                    )

            # Handle other errors
            else:

                return f"Gemini API error: {error_message}"

    return "Unable to generate a response."


# ----------------------------------
# STEP 3: GENERATE RAG ANSWER
# ----------------------------------

def generate_answer(query, retrieved_chunks):

    # Combine retrieved chunks into context
    context = "\n\n".join(retrieved_chunks)

    # Construct RAG prompt
    prompt = f"""
    You are an AI document assistant.

    Answer the user's question using ONLY the
    information provided in the context below.

    If the answer is not available in the context,
    clearly say that the information is not available
    in the uploaded document.

    Context:
    {context}

    User Question:
    {query}

    Answer:
    """

    # Generate answer using Gemini
    return generate_response(prompt)


# ----------------------------------
# STEP 4: GENERATE DOCUMENT SUMMARY
# ----------------------------------

def generate_summary(document_text):

    prompt = f"""
    You are an intelligent document summarisation assistant.

    Read the following document and generate a concise,
    well-structured summary.

    Include:

    1. Main topic
    2. Important concepts
    3. Key points
    4. Important conclusions

    Use clear and simple language.

    Document:
    {document_text}

    Summary:
    """

    # Generate summary using Gemini
    return generate_response(prompt)
# STEP 5: GENERATE INTERVIEW QUESTIONS

def generate_interview_questions(document_text):

    prompt = f"""
    You are an experienced technical interviewer.

    Analyse the following document and generate interview
    questions based on its content.

    Generate:

    1. Five basic conceptual questions.
    2. Five intermediate technical questions.
    3. Five advanced application-based questions.

    Provide a clear and accurate answer below each question.

    Use only the information available in the document.
    If a question requires information beyond the document,
    clearly mention that.

    Document:
    {document_text}

    Interview Questions and Answers:
    """

    return generate_response(prompt)