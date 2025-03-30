import pyautogui
import time

def print_mouse_position():
    while True:
        # Obtenir la position actuelle de la souris
        currentMouseX, currentMouseY = pyautogui.position()
        print('Position de la souris : X -', currentMouseX, ' Y -', currentMouseY)
        time.sleep(1)

print_mouse_position()