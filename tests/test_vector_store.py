
import sys
import os
import numpy as np

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from vector_store import create_vector_store, search_similar_chunks


def test_vector_store_creation():
    embeddings = np.array([
        [1.0, 0.0],
        [0.0, 1.0]
    ])

    index = create_vector_store(embeddings)

    assert index.ntotal == 2
    assert index.d == 2


def test_similarity_search():
    embeddings = np.array([
        [0.0, 0.0],
        [3.0, 4.0],
        [1.0, 0.0]
    ])

    chunks = ["Chunk A", "Chunk B", "Chunk C"]

    index = create_vector_store(embeddings)

    query_embedding = np.array([[0.1, 0.1]])

    results = search_similar_chunks(
        index,
        query_embedding,
        chunks,
        top_k=2
    )

    assert len(results) == 2
    assert results[0]["chunk"] == "Chunk A"
    assert results[1]["chunk"] == "Chunk C"
