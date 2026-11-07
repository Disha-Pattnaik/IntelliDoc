from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):

    try:
        reader = PdfReader(pdf_file)

        extracted_text = ""

        for page_number, page in enumerate(reader.pages, start=1):

            page_text = page.extract_text()

            if page_text:
                extracted_text += page_text + "\n"

        if not extracted_text.strip():
            raise ValueError("No readable text found in this PDF.")

        return extracted_text

    except Exception as e:
        raise Exception(f"PDF extraction failed: {e}")

def split_text_into_chunks(text, chunk_size=500, overlap=50):

    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Overlap must be non-negative and smaller than chunk size.")

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks   