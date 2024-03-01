import PIL.Image
import speech_to_text as STT
import screenshot
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold


global chat

CHAT_API_KEY = 'AIzaSyDhhT_uWRZOfqwyrIXZM_aKULa8IagRZu4'

#Given: String with text and image that wants to be said to API
#Returns: response string from API.
def send_message_with_image(message):
    img = PIL.Image.open('./screenshots/valorant.jpg')
    response = chat.send_message([message],
        safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }
 )
    return response

#Calls the gemini api to start the role play as AI Tenz.
def start_chat(map, hero):
    global chat
    genai.configure(api_key=CHAT_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    start_text = """Let's play a game where you role play as Tenz, and you will walk me through a game of Valorant.
     I am currently playing a game on the map {} as agent {}. I will tell you what is happening in the game.
     I want you to reply with what I should do as if you were Tenz. Limit your reply to 25 words. Speak as if you are coaching someone. Do not refer to me as my agent name.""".format(map, hero)
    return send_message_with_image(start_text)

#record a message and take a screenshot to send to AI.
def ask():
    #TODO
    screenshot.screenshot('image')
    message = STT.record_to_text()

    #sends message to bot with screenshot and question.
    send_message_with_image(message)
    return