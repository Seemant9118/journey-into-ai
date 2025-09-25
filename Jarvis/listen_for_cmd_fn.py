import speech_recognition as sr
from helper_fn import isInternetActive
from speak_fn import speak

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Listening for command...")
        audio = recognizer.listen(source)
    try:
        if isInternetActive():
            text = recognizer.recognize_google(audio).lower()
            print(f"You said: {text}")
            return text
        else:
            print('Please, Connect with Good Internet')
    except Exception as e:
        print(f"Error: {e}")
        return ""