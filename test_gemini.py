from gemini_service import generate_answer

query = "What are the different types of machine learning?"

retrieved_chunks = [
    "Supervised learning uses labelled data to train models.",
    "Unsupervised learning identifies hidden patterns in data without labelled examples."
]

print("Testing Gemini with retrieved document context...")

answer = generate_answer(query, retrieved_chunks)

print("\nGenerated Answer:")
print(answer)