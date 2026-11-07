import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Validate API key
if not GEMINI_API_KEY:
    raise ValueError(
        "Gemini API key not found. Please check your .env file."
    )

print("Configuration loaded successfully!")