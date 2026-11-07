import sys
import os
import numpy as np
import pytest

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from vector_store import (
    create_vector_store,
    search_similar_chunks
)


# VECTOR STORE CREATION

def test_vector_store_creation():
    embeddings = np.array([
        [1.0, 0.0],
        [0.0, 1.0]
    ])

    index = create_vector_store(embeddings)

    assert index.ntotal == 2
    assert index.d == 2


# SIMILARITY SEARCH

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


def test_similarity_distance():
    embeddings = np.array([
        [0.0, 0.0],
        [3.0, 4.0]
    ])

    chunks = ["Chunk A", "Chunk B"]

    index = create_vector_store(embeddings)

    query_embedding = np.array([[0.0, 0.0]])

    results = search_similar_chunks(
        index,
        query_embedding,
        chunks,
        top_k=1
    )

    assert results[0]["distance"] == pytest.approx(0.0)


def test_top_k_larger_than_vectors():
    embeddings = np.array([
        [0.0, 0.0],
        [1.0, 1.0]
    ])

    chunks = ["Chunk A", "Chunk B"]

    index = create_vector_store(embeddings)

    query_embedding = np.array([[0.1, 0.1]])

    results = search_similar_chunks(
        index,
        query_embedding,
        chunks,
        top_k=5
    )

    assert len(results) == 2


def test_empty_vector_store():
    embeddings = np.empty((0, 2), dtype="float32")

    index = create_vector_store(embeddings)

    assert index.ntotal == 0
    assert index.d == 2


def test_empty_vector_search():
    embeddings = np.empty((0, 2), dtype="float32")

    index = create_vector_store(embeddings)

    results = search_similar_chunks(
        index,
        np.array([[0.1, 0.1]]),
        [],
        top_k=3
    )

    assert results == []