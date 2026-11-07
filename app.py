
import streamlit as st

from agent_service import run_agent

from pdf_processor import (
    extract_text_from_pdf,
    split_text_into_chunks
)

from embedding_service import generate_embeddings

from vector_store import (
    create_vector_store,
    search_similar_chunks
)

from gemini_service import (
    generate_answer,
    generate_summary,
    generate_interview_questions
)


# ----------------------------------
# PAGE CONFIGURATION
# ----------------------------------

st.set_page_config(
    page_title="IntelliDoc",
    page_icon="📚",
    layout="wide"
)


# ----------------------------------
# APPLICATION TITLE
# ----------------------------------

st.title("📚 IntelliDoc")

st.subheader("AI-Powered Document Assistant")

st.write(
    "Upload a PDF document and ask questions "
    "to get intelligent, context-aware answers."
)


# ----------------------------------
# PDF UPLOAD
# ----------------------------------

uploaded_file = st.file_uploader(
    "Upload your PDF document",
    type=["pdf"]
)


# ----------------------------------
# PROCESS PDF
# ----------------------------------

if uploaded_file is not None:

    if st.button("Process PDF"):

        with st.spinner("Processing your document..."):

            try:

                text = extract_text_from_pdf(uploaded_file)

                chunks = split_text_into_chunks(
                    text,
                    chunk_size=500,
                    overlap=50
                )

                embeddings = generate_embeddings(chunks)

                index = create_vector_store(embeddings)

                st.session_state.chunks = chunks
                st.session_state.document_text = text
                st.session_state.index = index
                st.session_state.filename = uploaded_file.name

                st.success("PDF processed successfully!")

                st.write("Uploaded file:", uploaded_file.name)

                st.write("Total chunks:", len(chunks))

                st.write(
                    "Embedding dimensions:",
                    embeddings.shape[1]
                )

            except Exception as e:

                st.error(f"Error processing PDF: {e}")


# ----------------------------------
# DOCUMENT SUMMARISATION
# ----------------------------------

if "document_text" in st.session_state:

    st.divider()

    st.subheader("📄 Document Summarisation")

    if st.button("Summarise Document"):

        with st.spinner("Generating document summary..."):

            try:

                summary = generate_summary(
                    st.session_state.document_text
                )

                st.subheader("Document Summary")

                st.write(summary)

            except Exception as e:

                st.error(f"Error generating summary: {e}")


# ----------------------------------
# INTERVIEW QUESTION GENERATOR
# ----------------------------------

if "document_text" in st.session_state:

    st.divider()

    st.subheader("🎯 AI Interview Question Generator")

    if st.button("Generate Interview Questions"):

        with st.spinner("Generating interview questions..."):

            try:

                questions = generate_interview_questions(
                    st.session_state.document_text
                )

                st.subheader("Interview Questions and Answers")

                st.write(questions)

            except Exception as e:

                st.error(f"Error generating questions: {e}")


# ----------------------------------
# AGENTIC AI ASSISTANT
# ----------------------------------

if "index" in st.session_state:

    st.divider()

    st.subheader("🤖 IntelliDoc AI Agent")

    agent_request = st.text_input(
        "Give IntelliDoc a task:",
        placeholder="Example: Summarise my document and prepare interview questions."
    )

    if st.button("Run AI Agent"):

        if agent_request.strip():

            with st.spinner("AI Agent is analysing your request..."):

                try:

                    response = run_agent(
                        agent_request,
                        st.session_state.document_text,
                        st.session_state.chunks,
                        st.session_state.index
                    )

                    st.subheader("AI Agent Response")

                    st.write(response)

                except Exception as e:

                    st.error(f"Agent execution failed: {e}")

        else:

            st.warning("Please enter a task.")


# ----------------------------------
# QUESTION INPUT - RAG
# ----------------------------------

if "index" in st.session_state:

    st.divider()

    st.subheader("Ask Questions About Your PDF")

    query = st.text_input(
        "Enter your question:"
    )

    if st.button("Ask IntelliDoc"):

        if query.strip():

            with st.spinner(
                "Searching document and generating answer..."
            ):

                try:

                    query_embedding = generate_embeddings([query])

                    results = search_similar_chunks(
                        st.session_state.index,
                        query_embedding,
                        st.session_state.chunks,
                        top_k=3
                    )

                    retrieved_chunks = [
                        result["chunk"] for result in results
                    ]

                    answer = generate_answer(
                        query,
                        retrieved_chunks
                    )

                    st.subheader("🤖 IntelliDoc Answer")

                    st.write(answer)

                    with st.expander("View Retrieved Text Chunks"):

                        for i, result in enumerate(results, start=1):

                            st.write(f"Chunk {i}")

                            st.write(result["chunk"])

                            st.write(
                                "Distance:",
                                result["distance"]
                            )

                            st.divider()

                except Exception as e:

                    st.error(f"Error generating answer: {e}")

        else:

            st.warning("Please enter a question.")