# this will take a screenshot of the whole screen and save it as png format
import pyautogui
myScreenshot = pyautogui.screenshot()
myScreenshot.save(
    r'C:\Users\Aviral\Documents\PyScreenshots\scshot' + str(counter) + '.png')
