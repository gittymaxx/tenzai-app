import time
import keyboard
import chat_ai as ai
import text_to_speech as tts

#MODIFIABLE GLOBAL VARIABLES
map = "Lotus"
hero = "Phoenix"

#things to do when we start the program. Waits for the user to press the 'n' or 'N' key.
def start_program():
    ai.start_chat(map, hero)
    print("press N to start the program.")
    while(True):
        pressed = keyboard.read_key()
        if pressed == "n" or pressed == "N":
            return 
        time.wait(.1)


if __name__ == "__main__":
    intro = "Hi, I'm Tenz AI. Here to help you win in Valorant. it looks like you're playing on {}, with {}. Focus up, let's do this!".format(map, hero)
    start_program()
    tts.say(intro)

    while(True):
        pressed = keyboard.read_key()
        if pressed == "n" or pressed == "N":
            ai.ask()
        time.wait(.3)
