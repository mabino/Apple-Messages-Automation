import pyautogui
import cv2
import numpy as np

# Find the location of the Messages app icon and click it
messages_icon = pyautogui.locateOnScreen('messages_icon.png')
pyautogui.click(messages_icon)

pyautogui.sleep(3)

# Find the search bar and click it
search_bar = pyautogui.locateOnScreen('search_bar.png')
pyautogui.click(search_bar)

# Type the search terms
pyautogui.typewrite('Contact First Name')

pyautogui.sleep(2)

# Find the contact in the results and click it
target_contact = pyautogui.locateOnScreen('contact.png')
pyautogui.click(target_contact)

pyautogui.sleep(2)

# Find the message input and click it
message_input = pyautogui.locateOnScreen('message_input.png')
pyautogui.click(message_input)

# Type and send the message
pyautogui.typewrite('Hello!')
pyautogui.press('enter')
