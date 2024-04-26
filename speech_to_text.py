import time
import sounddevice as sd
from scipy.io.wavfile import write
import keyboard
import requests


recording_folder = './recordings/'
API_KEY = ""


#calls API to transform output file to text
def transform_speech():

    # API endpoint configuration
    api_url = "https://transcribe.whisperapi.com"
    headers = {'Authorization': 'Bearer {}'.format(API_KEY)}

    # Payload setup for API request
    payload = {
        'file': {'file': open('{}my_question.wav'.format(recording_folder), 'rb')},
        'data': {
            "fileType": "wav",  # Default is 'wav'.
            "diarization": "false",  # 'True' may slow down processing.
            "numSpeakers": "1",  # Optional: Number of speakers for diarization. If blank, model will auto-detect.
            #"url": "URL_OF_STORED_AUDIO_FILE",  # Use either URL or file, not both.
            "initialPrompt": "",  # Optional: Teach model a phrase. May negatively impact results.
            "language": "en",  # Optional: Language of speech. If blank, model will auto-detect.
            "task": "transcribe",  # Use 'translate' to translate speech from language to English. Transcribe is default.
            "callbackURL": "",  # Optional: Callback URL for results to be sent.
        }
    }

    # Ensure the 'callbackURL' starts with 'https://' and does not include 'www.'
    # The server calls the callback URL once the response is ready.

    # Make the API request and print the response
    response = requests.post(api_url, headers=headers, files=payload['file'], data=payload['data'])
    # Note: Omitting a parameter or setting it as an empty string "" allows for auto-detection.
    # Keep in mind that auto-detected values may not always be accurate.

    return response.text

def record_speech():
    time.sleep(1)
    fs = 44100  # Sample rate
    try: 
        recording = sd.rec(frames = 10 * fs, samplerate=fs, channels=2)
        print("Now recording")
        while True:
            pressed = keyboard.read_key()
            if pressed == "n" or pressed == "N":
                print("Finished Recording")
                raise KeyboardInterrupt
            time.sleep(.3)
    except KeyboardInterrupt:
        write('{}my_question.wav'.format(recording_folder), fs, recording)  # Save as WAV file 

def record_to_text():
    record_speech()
    return transform_speech()
  