import time
import keyboard
import pyautogui

#MODIFIABLE GLOBAL VARIABLES
map = "Lotus"
hero = "Phoenix"


#UNMODDABLE CONSTANTS
screenshot_folder = "./screenshots"



#takes screenshot and saves it under the name sent
def screenshot(screenshot_name):
    screenshot = pyautogui.screenshot()
    screenshot.save('{}/{}.png'.format(screenshot_folder, screenshot_name))


#Given: String with text we want to be said.
#Returns: MP3 with playable Sound.
def get_recording_from_text(text):
    #TODO IMPLEMENTATION OF API

    return

#Given: String with text that wants to be said. Say Sound.
#Returns: Nothing when finished
def say(text):

    #sends text and expects recording back
    recording = get_recording_from_text(text)

    #TODO PLAYS RECORDING BACK.
    return


#Given: String with text that wants to be said to API
#Returns: resonse string from API.
def send_message(message):
    response = ""
    return response



#Calls the API with gemini to start the role_play as AI Tenz.
def start_chat():
    start_text = "Let's play a game where you role play as Tenz"
    send_message(start_text)


#things to do when we start the program. Waits for the user to press the 'n' or 'N' key.
def start_program():
    start_chat()
    while(True):
        print("press N to start the program.")
        pressed = keyboard.read_key()
        if pressed == "n" or pressed == "N":
            return 
        time.wait(.3)


#record a message and take a screenshot to send to AI.
def ask_ai():
    #TODO
    return

if __name__ == "__main__":
    intro = "Hi, I'm Tenz AI. Here to help you win in Valorant. it looks like you're playing on {}, with {}. Focus up, let's do this!".format(map, hero)
    start_program()
    say(intro)

    while(True):
        pressed = keyboard.read_key()
        if pressed == "n" or pressed == "N":
            ask_ai()
            time.wait(15)
        time.wait(.3)
