import pyautogui

print(pyautogui.size())  # Get the screen size
print(pyautogui.position())  # Get the current mouse position
pyautogui.moveTo(1879,19,3)  # Move the mouse to (1879, 19) over 3 seconds
pyautogui.click(1879, 19,3,3, button="left")  # Perform a mouse click