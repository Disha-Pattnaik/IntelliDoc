import faiss
import numpy as np


def create_vector_store(embeddings):

    # Convert embeddings into NumPy array
    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    # Get embedding dimensions
    dimension = embeddings.shape[1]

    # Create FAISS index using L2 distance
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings to FAISS
    index.add(embeddings)

    return index
def search_similar_chunks(index, query_embedding, chunks, top_k=3):

    # Convert query embedding into NumPy array
    query_embedding = np.array(
        query_embedding,
        dtype="float32"
    )

    # Perform similarity search
    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    # Retrieve matching chunks
    for i in range(len(indices[0])):

        chunk_index = indices[0][i]

        if chunk_index == -1:
            continue

        results.append({
            "chunk": chunks[chunk_index],
            "distance": float(distances[0][i])
        })

    return results