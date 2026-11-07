
import pytest
import sys
import os
from io import BytesIO
from pypdf import PdfWriter

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from pdf_processor import (
    split_text_into_chunks,
    extract_text_from_pdf
)


# CHUNK CREATION TESTS

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


def test_chunk_overlap():
    text = "A" * 1000

    chunks = split_text_into_chunks(
        text,
        chunk_size=500,
        overlap=50
    )

    assert chunks[0][-50:] == chunks[1][:50]


def test_short_text():
    text = "Hello World"

    chunks = split_text_into_chunks(text)

    assert len(chunks) == 1
    assert chunks[0] == text


def test_empty_text():
    chunks = split_text_into_chunks("")

    assert chunks == []


# INPUT VALIDATION TESTS

def test_invalid_chunk_size():
    with pytest.raises(ValueError):
        split_text_into_chunks(
            "Hello World",
            chunk_size=0
        )


def test_negative_chunk_size():
    with pytest.raises(ValueError):
        split_text_into_chunks(
            "Hello World",
            chunk_size=-10
        )


def test_invalid_overlap():
    with pytest.raises(ValueError):
        split_text_into_chunks(
            "Hello World",
            chunk_size=500,
            overlap=500
        )


def test_negative_overlap():
    with pytest.raises(ValueError):
        split_text_into_chunks(
            "Hello World",
            chunk_size=500,
            overlap=-10
        )


# PDF EXTRACTION TESTS

def test_invalid_pdf():
    invalid_pdf = BytesIO(b"This is not a valid PDF")

    with pytest.raises(Exception):
        extract_text_from_pdf(invalid_pdf)


def test_empty_pdf():
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)

    pdf_file = BytesIO()
    writer.write(pdf_file)
    pdf_file.seek(0)

    with pytest.raises(Exception):
        extract_text_from_pdf(pdf_file)