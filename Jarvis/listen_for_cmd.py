import speech_recognition as sr
from speak import speak
from helper_fn import isInternetActive

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for command...")
        audio = recognizer.listen(source)
    try:
        if isInternetActive():
            return recognizer.recognize_google(audio).lower()
        else:
            print('Jarvis: Please use stable Internet')
    except Exception as e:
        print(f"Error: {e}")
        return ""
