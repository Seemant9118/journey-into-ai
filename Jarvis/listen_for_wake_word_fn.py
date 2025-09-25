import speech_recognition as sr

def listen_for_wake_word(wake_word="jarvis"):
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Say Jarvis to activate")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"You said: {text}")

            if wake_word in text:
                print("Jarvis activated")
                return True

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Speech recognition service error")
