import os
from dotenv import load_dotenv
from google import genai

# Load .env file
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
        model="gemini-2.5-flash",
        contents=question
    )
    return response.text


if __name__ == "__main__":
    print("Testing Gemini...")
    print(ask_gemini("Who is the Prime Minister of India?"))