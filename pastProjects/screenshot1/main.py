# this will take a screenshot of the whole screen and save it as png format
import pyautogui
myScreenshot = pyautogui.screenshot()
counter = 1
myScreenshot.save(r'C:\Users\Aviral\Documents\scshot' + str(counter) + '.png')
