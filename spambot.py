#encoding: utf-8

import pyautogui, sys, keyboard, time

def textboxCoordinates():
    """
    Function that returns textbox coordinates.
    
    Returns
    -----
    text - Textbox coordinates.
    """
    print("Go to chat textbox")
    time.sleep(3)
    text = pyautogui.position()
    print("Chat position acquired: {}".format(text))
    return text

def buttonCooordinates():
    """
    Function that returns send button coordinates.

    Returns
    -----
    button - Send button coordinates.
    """
    print("Go to send button")
    time.sleep(3)
    button = pyautogui.position()
    print("Send button position acquired: {}".format(button))
    return button

def run(text, button, msg, interval):
    """
    Function that does the spam of user messages.

    Parameters
    -----
    text - Textbox position.
    button - Send button position.
    msg - Message to spam.
    interval - Interval between messages.
    """
    n = 1
    while not keyboard.is_pressed('esc'): #Ends when esc is pressed
        pyautogui.click(text)
        pyautogui.typewrite(msg, interval=interval)
        pyautogui.click(button)
        print("Message number:{}".format(n))
        n += 1

#########################################################
#                                                       #
#                          MAIN                         #
#                                                       #
#########################################################

msg = input("Message to spam: ")
interval = float(input(("Interval between messages: ")))
text = textboxCoordinates()
button = buttonCooordinates()
run(text, button, msg, interval)
