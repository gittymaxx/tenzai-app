import time
import sounddevice as sd
from scipy.io.wavfile import write
import keyboard




recording_folder = './recordings/'
API_KEY = ""


#calls API to transform output file to text
def transform_speech():
    #TODO
    return ""

#records the speech and turns it into file output.wav
def record_speech():
    fs = 44100  # Sample rate
    try: 
        recording = sd.rec(None, samplerate=fs, channels=2)
        while True:
            pressed = keyboard.read_key()
            if pressed == "n" or pressed == "N":
                raise KeyboardInterrupt
            time.wait(.3)
    except KeyboardInterrupt:
        write('{}output.wav'.format(recording_folder), fs, recording)  # Save as WAV file 

def record_to_text():
    record_speech()
    return transform_speech()
