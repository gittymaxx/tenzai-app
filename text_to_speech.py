import requests
from playsound import playsound 
TTS_API_KEY = "69fbd62afbc20a879804a57f8beccdcb"

#Given: String with text we want to be said.
#Returns: MP3 with playable Sound.
def get_recording_from_text(text, filename):

    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/LCMj3x3tih2eXFZcAv2Z"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "69fbd62afbc20a879804a57f8beccdcb"
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)
    with open('{}.mp3'.format(filename), 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)


def say_prepped(filename):
    #TODO PLAY FILENAME
    return

def prep(text, filename):
    get_recording_from_text(text, filename)



#Given: String with text that wants to be said.
#Returns: Nothing when finished
def say(text):

    #sends text and expects recording back
    get_recording_from_text(text)

    playsound('output.wav')

    #TODO PLAYS RECORDING BACK.
    return