import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Ask user for a question
question = input("Ask Gemini: ")

# Send question to Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question
)

# Print answer
print("\nGemini Answer:\n")
print(response.text)