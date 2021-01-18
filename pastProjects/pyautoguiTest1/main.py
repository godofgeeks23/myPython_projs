# pyautogui mouse and keyboard automation tested out
import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print("Screen Size: " + str(screenWidth) + "," + str(screenHeight))
print("mouse: " + str(currentMouseX) + "," + str(currentMouseY))
# pyautogui.moveTo(100, 150)  # Move the mouse.
# pyautogui.click()
# pyautogui.click(200, 220)  # Click at the x, y.
# pyautogui.move(0, 10)  # mouse 10 px down rel to its current position.
# pyautogui.doubleClick()
# pyautogui.moveTo(500, 500, duration=1, tween=pyautogui.easeInOutQuad)
# pyautogui.write('Hello world!', interval=0.25)   # Type with pause b/w keys.
# pyautogui.press('esc')
# pyautogui.keyDown('shift')
# pyautogui.write(['left', 'left', 'left'], interval=0.15)
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'n')
pyautogui.alert('This is an alert box.')
# pyautogui.confirm('Shall I proceed?')
# pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
# pyautogui.prompt('What is your name?')
# pyautogui.password('Enter password (text will be hidden)')
