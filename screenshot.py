
#UNMODDABLE CONSTANTS
screenshot_folder = "./screenshots"

#takes screenshot and saves it under the name sent
def screenshot(screenshot_name):
    screenshot = pyautogui.screenshot()
    screenshot.save('{}/{}.png'.format(screenshot_folder, screenshot_name))
