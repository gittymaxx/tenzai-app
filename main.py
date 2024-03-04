import time
import os
import keyboard
import chat_ai as ai
import text_to_speech as tts

#MODIFIABLE GLOBAL VARIABLES
map = "Breeze"
hero = "Phoenix"

#UNMODIFIABLE VARIABLES
FIRST_LINE = 'first_line'
INTRO = 'intro'

intro_line = "Hi, I'm Tenz AI. Here to help you win in Valorant. it looks like you're playing on {}, with {}. Focus up, let's do this!".format(map, hero)

#things to do when we start the program. sleeps for the user to press the 'n' or 'N' key.
def start_program():
    response = ai.start_chat(map, hero)
    tts.prep(response, FIRST_LINE)
    tts.prep(intro_line, INTRO)
    print("press N to start the program.")
    while(True):
        pressed = keyboard.read_key()
        if pressed == "n" or pressed == "N":
            return 
        time.sleep(.1)


if __name__ == "__main__":
    start_program()
    tts.say_recorded(INTRO)
    time.sleep(3)
    tts.say_recorded(FIRST_LINE)
    while(True):
        pressed = keyboard.read_key()
        if pressed == "n" or pressed == "N":
            if os.path.isfile("output.mp3"):
                os.remove("output.mp3")
            print("you've pressed the button")
            ai.ask()
        time.sleep(.3)
