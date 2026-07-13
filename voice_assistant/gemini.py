import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def ask_gemini(question):
    """
    Sends a question to Gemini and returns the answer.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=question
    )

    return response.text