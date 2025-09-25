from speak_fn import speak
import webbrowser
import pygame
import os
import time
import requests
from listen_for_cmd_fn import listen_for_command
from openai import OpenAI

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def open_website(url,name):
    speak(f"Opening {name}..")
    webbrowser.open(url)

def play_music():
    # Resolve absolute path to mp3 file
    filename = os.path.join(os.path.dirname(__file__), "public", "under_world.wav")

    if not os.path.isfile(filename):
        speak("Sorry, I cannot find the music file.")
        print("File not found:", filename)
        return

    try:
        # Initialize pygame completely (important!)
        pygame.init()
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

        speak("Playing music...")

        # Load and play
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Keep program alive while playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    except Exception as e:
        print("Music playback error:", e)
        speak("I couldn't play the music due to an error.")

    finally:
        pygame.mixer.quit()
        pygame.quit()

def fetch_news():
    api_key = '30626bacd2b74c29b3a4041e00aa1da7'
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    speak("Fetching the today's latest news")
    try:
        response = requests.get(url)
        data = response.json()

        headlines = [article['title'] for article in data['articles'][:5]]
        return headlines
    except Exception as e:
        return [f"Error fetching news: {e}"]

def ai_res():
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(
        api_key=api_key
    )

    response = client.responses.create(
        model="gpt-5",
        input="Write a short bedtime story about a unicorn."
    )
    print(response.output_text)




def handle_command(command):
    if "open google" in command:
        open_website("https://www.google.com", "Google")
    elif "open youtube" in command:
        open_website("https://www.youtube.com","Youtube")
    elif "play music" in command:
        play_music()
    elif "news" in command:
        headlines = fetch_news()
        for h in headlines:
            speak(h)
    elif "stop" in command:
        speak("Okay, shutting down. Goodbye!")
        exit(0)
    else:
        ai_res()
        # speak("Sorry, I didn’t understand that.")

