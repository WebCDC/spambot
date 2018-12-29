import pyautogui, sys
import keyboard
import time

print("Go to chat textbox")
time.sleep(3)
text = pyautogui.position()
print("Chat position acquired: {}".format(text))

print("Go to send button")
time.sleep(3)
button = pyautogui.position()
print("Send button position acquired: {}".format(button))

print("Starting...")
n = 1

while not keyboard.is_pressed('esc'):
    pyautogui.click(text)
    pyautogui.typewrite("spam", interval=0.1)
    pyautogui.click(button)
    print("Message number: {}".format(n))
    n += 1
