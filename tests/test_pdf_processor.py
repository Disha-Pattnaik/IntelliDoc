import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pdf_processor import split_text_into_chunks


def test_chunk_creation():

    text = "A" * 1200

    chunks = split_text_into_chunks(
        text,
        chunk_size=500,
        overlap=50
    )

    assert len(chunks) == 3


def test_chunk_size():

    text = "A" * 1000

    chunks = split_text_into_chunks(
        text,
        chunk_size=500,
        overlap=50
    )

    assert len(chunks[0]) == 500


def test_invalid_chunk_size():

    with pytest.raises(ValueError):

        split_text_into_chunks(
            "Hello World",
            chunk_size=0
        )


def test_invalid_overlap():

    with pytest.raises(ValueError):

        split_text_into_chunks(
            "Hello World",
            chunk_size=500,
            overlap=500
        )