from helper_fn import isInternetActive
import pygame
from gtts import gTTS
import os
import time

def speak(text):
    if isInternetActive():
        tts = gTTS(text=text, lang="en")
        filename = f"temp_{int(time.time())}.mp3"
        tts.save(filename)

        pygame.mixer.init()
        print(f"Jarvis: {tts.text}") # print text
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play() # speak text

        # Wait until the music stops playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()
        os.remove(filename)
    else:
        print('Please, Connect with Good Internet')