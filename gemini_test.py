import os
import traceback
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("Gemini API Test")
print("=" * 50)
print("API Key:", api_key if api_key else "Not Found")

try:
    # Create Gemini client
    client = genai.Client(api_key=api_key)
    print("Client created successfully.")

    # Send a test prompt
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Who is the Prime Minister of India?"
    )

    print("\n Gemini Response:")
    print(response.text)

except Exception:
    print("\n Error occurred:")
    traceback.print_exc()