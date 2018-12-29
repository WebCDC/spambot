import pyautogui, sys
import keyboard
import time

print("Coordenadas da textbox do chat")
time.sleep(3)
text = pyautogui.position()
print("Coordenadas do botão de enviar")
time.sleep(3)
but = pyautogui.position()

print("Iniciar")
n = 1

while not keyboard.is_pressed('esc'):
    pyautogui.click(text)#position of chatbox
    pyautogui.typewrite("spam", interval=0.1)
    pyautogui.click(but)#position of end button
    print(n)
    n += 1
