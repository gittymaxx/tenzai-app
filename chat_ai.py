import speech_to_text as STT
import screenshot



#Given: String with text that wants to be said to API
#Returns: response string from API.
def send_message(message):
    #TODO
    response = ""
    return response

#Calls the gemini api to start the role play as AI Tenz.
def start_chat():
    start_text = "Let's play a game where you role play as Tenz"
    send_message(start_text)

#record a message and take a screenshot to send to AI.
def ask():
    #TODO
    screenshot.screenshot('image')
    message = STT.record_to_text()

    #sends message to bot with screenshot and question.
    send_message(message)
    return