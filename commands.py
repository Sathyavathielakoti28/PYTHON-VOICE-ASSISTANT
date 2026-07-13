from gemini import ask_gemini
from speak import speak
import webbrowser
from datetime import datetime
import os


def process_command(text):
    """
    Processes the user's spoken or typed command.
    """

    text = text.lower().strip()

    print("Processing command:", text)

    # Greeting
    if "hello" in text:
        speak("Hello! How are you?")

    # Assistant name
    elif "your name" in text or "who are you" in text:
        speak("I am your Python Voice Assistant.")

    # Open websites
    elif "open youtube" in text:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in text:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open gmail" in text:
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com")

    elif "open chatgpt" in text:
        speak("Opening ChatGPT.")
        webbrowser.open("https://chatgpt.com")

    elif "open linkedin" in text:
        speak("Opening LinkedIn.")
        webbrowser.open("https://www.linkedin.com")

    # Open applications
    elif "open calculator" in text:
        speak("Opening Calculator.")
        os.system("calc")

    elif "open notepad" in text:
        speak("Opening Notepad.")
        os.system("notepad")

    elif "open visual studio code" in text or "open vscode" in text:
        speak("Opening Visual Studio Code.")
        os.system("code")

    # Time
    elif "time" in text:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    # Date
    elif "date" in text:
        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    # Google Search
    elif "search google for" in text:
        query = text.replace("search google for", "").strip()

        if query:
            speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("Please tell me what you want to search.")

    # Exit
    elif "exit" in text or "quit" in text:
        speak("Goodbye!")
        exit()

    # Gemini AI
    else:
        print("Sending question to Gemini...")

        try:
            answer = ask_gemini(text)
            print("Gemini:", answer)
            speak(answer)

        except Exception as e:
            print("Gemini Error:", e)
            speak("Sorry, I couldn't connect to Gemini.")