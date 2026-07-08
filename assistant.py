from speak import speak
from listen import listen
from commands import process_command

def main():
    """
    Main function that runs the voice assistant continuously.
    """

    speak("Hello! I am your Python Voice Assistant.")

    while True:
        text = input("enter your command: ")

        if not text:
            continue

        print("You said:", text)

        process_command(text)


if __name__ == "__main__":
    main()