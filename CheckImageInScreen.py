import pyautogui


# left click on the position of the image windowsButton
pyautogui.click(pyautogui.locateOnScreen(
    'windowsButton.png', confidence=0.9), duration=0.5)

# type "calculator" and press enter
pyautogui.typewrite('calculator', interval=0.1)
pyautogui.press('enter')
# wait for the calculator to open
pyautogui.sleep(0.5)
pyautogui.click(pyautogui.locateOnScreen(
    '7.png', confidence=0.9))
pyautogui.click(pyautogui.locateOnScreen(
    'plus.png', confidence=0.9))
pyautogui.click(pyautogui.locateOnScreen(
    '7.png', confidence=0.9))
pyautogui.click(pyautogui.locateOnScreen(
    'equal.png', confidence=0.9))
pyautogui.click(pyautogui.locateOnScreen(
    'c.png', confidence=0.9))
