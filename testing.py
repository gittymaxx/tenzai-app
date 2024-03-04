import time
import sounddevice as sd
from scipy.io.wavfile import write

recording_folder = './recordings/'
API_KEY = "6G2IDAFKJZFX675PZ983VFGNTDFSJM2L"

import keyboard
import chat_ai as ai
import text_to_speech as tts

#MODIFIABLE GLOBAL VARIABLES
map = "Lotus"
hero = "Phoenix"

#things to do when we start the program. sleeps for the user to press the 'n' or 'N' key.
def start_program():
    ai.start_chat(map, hero)
    print("press N to start the program.")
    while(True):
        pressed = keyboard.read_key()
        if pressed == "n" or pressed == "N":
            return 
        time.sleep(.1)

#records the speech and turns it into file output.wav
def record_speech():
    fs = 44100  # Sample rate
    try: 
        recording = sd.rec(frames = 20*fs, samplerate=fs, channels=2)
        while True:
            pressed = keyboard.read_key()
            if pressed == "n" or pressed == "N":
                raise KeyboardInterrupt
            time.sleep(.3)
    except KeyboardInterrupt:
        write('{}output.wav'.format(recording_folder), fs, recording)  # Save as WAV file 

# if __name__ == "__main__":
#     intro = "Hi, I'm Tenz AI. Here to help you win in Valorant. it looks like you're playing on {}, with {}. Focus up, let's do this!".format(map, hero)
#     start_program()
#     tts.say(intro)

#     while(True):
#         pressed = keyboard.read_key()
#         if pressed == "n" or pressed == "N":
#             record_speech()
#         time.sleep(.3)
    
record_speech()