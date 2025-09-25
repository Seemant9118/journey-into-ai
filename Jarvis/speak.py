from gtts import gTTS
import pygame
import os
import time
from helper_fn import isInternetActive

def speak(text): 
    if isInternetActive(): 
        tts = gTTS(text=text, lang="en") 
        filename = f"temp_{int(time.time())}.mp3" 
        tts.save(filename) 
        pygame.mixer.init() 
        pygame.mixer.music.load(filename) 

        print(text)
        pygame.mixer.music.play() # Wait until the music stops playing 

        while pygame.mixer.music.get_busy(): 
            time.sleep(0.1) 
            
        pygame.mixer.quit() 
        os.remove(filename) 
    else: 
        print('Jarvis: Please use stable Internet')