import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

def listen():
    """
    Listens through the microphone and converts speech into text.
    """
    with sr.Microphone() as source:
        print("Listening... Please speak.")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand you."
    except sr.RequestError:
        return "Internet connection problem."