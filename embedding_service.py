from sentence_transformers import SentenceTransformer


# Load the pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks):

    # Convert text chunks into numerical vectors
    embeddings = model.encode(chunks)

    return embeddings