from gtts import gTTS
from pynput import keyboard
import os
import threading

stop_playing = False

def on_press(key):
    global stop_playing
    if key == keyboard.Key.space:
        stop_playing = True

def play_text():
    tts = gTTS(text='A chair is a type of seat, typically designed for one person and consisting of one or more legs, a flat or slightly angled seat and a back-rest. They may be made of wood, metal, or synthetic materials, and may be padded or upholstered in various colors and fabrics.', lang='en')
    tts.save("hello.mp3")
    while not stop_playing:
        os.system("mpg321 hello.mp3")

listener = keyboard.Listener(on_press=on_press)
listener.start()

play_thread = threading.Thread(target=play_text)
play_thread.start()
