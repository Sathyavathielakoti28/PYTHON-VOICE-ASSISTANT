import pyttsx3

def speak(prompt):
    engine = pyttsx3.init()

    engine.say(prompt)
    engine.runAndWait()
    engine.stop()