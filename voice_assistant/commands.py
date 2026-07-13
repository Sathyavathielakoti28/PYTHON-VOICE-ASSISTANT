from gemini import ask_gemini
from speak import speak
import webbrowser
from datetime import datetime
import os

def process_command(text):
    """
    Processes the user's spoken or typed command.
    """

    # Convert the command to lowercase
    text = text.lower()

    print("Processing command:", text)

    # Greeting
    if "hello" in text:
        print("Matched: hello")
        speak("Hello! How are you?")

    # Tell assistant's name
    elif "your name" in text or "who are you" in text:
        print("Matched: your name")
        speak("I am your Python Voice Assistant.")

    # Open YouTube
    elif "open youtube" in text:
        print("Matched: open youtube")
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    # Open Google
    elif "open google" in text:
        print("Matched: open google")
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    # Tell current time
    elif "time" in text:
        print("Matched: time")
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    # Tell today's date
    elif "date" in text:
        print("Matched: date")
        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")
    
    elif "open calculator" in text:
        speak("Opening Calculator")
        os.system("calc")
        
    elif "open notepad" in text:
        speak("Opening Notepad")
        os.system("notepad")
        
    elif "open visual studio code" in text or "open vscode" in text:
        speak("Opening Visual Studio Code")
        os.system("code") 
    
    elif "open gmail" in text:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
        
    elif "open chatgpt" in text:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")
        
    elif "open linkedin" in text:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")  
        
    elif "search google for" in text:
        query = text.replace("search google for", "")
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}") 
        
    elif "exit" in text or "quit" in text:
        speak("Goodbye!")
        exit()
    # Unknown command
    else:
        print("Sending question to Gemini...")
        answer = ask_gemini(text)
        print("Gemini:", answer)
        speak(answer)