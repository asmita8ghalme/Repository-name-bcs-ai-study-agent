import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Find the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the .env file
load_dotenv(BASE_DIR / ".env")

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key is found
if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in the .env file.")

# Connect to Gemini
client = genai.Client(api_key=api_key)


def ask_gemini(question):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    )

    return response.text