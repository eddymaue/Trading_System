import pyautogui
import pyperclip
from keyboard import press_and_release
import time
import sys
import ast
import os

def PlaceSymbolesOnMQchart(symbols_list):
    # Sauvegarder la position initiale de la souris
    mX, mY = pyautogui.position()
    i = 0

    for couple in data:
        x, y = couple

        if i < len(symbols_list):
            Symb = symbols_list[i]
            print(f"Placing symbol: {Symb} at position ({x}, {y})")

            # Déplacer et cliquer
            pyautogui.moveTo(x, y)
            pyautogui.click()

            # Taper directement le symbole
            pyautogui.typewrite(Symb)
            time.sleep(1)  # Augmenter le délai ici
            pyautogui.press('enter')
            time.sleep(1)  # Augmenter le délai ici
        i += 1

    # Retourner à la position d'origine
    pyautogui.moveTo(mX, mY)
    if sys.argv[3] == "1":  # lClickPositionOriginal
        pyautogui.click()

# Code principal
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python MouseAutomation.py <file.txt> <confirmation> <clickOriginal> <symbols>")
        sys.exit(1)

    lcFileTxtName = sys.argv[1]
    symbols_arg = sys.argv[4]
    symbols_list = symbols_arg.split()

    # Vérifier si le fichier de positions existe
    if not os.path.exists(lcFileTxtName):
        print(f"Erreur: Le fichier {lcFileTxtName} n'existe pas.")
        sys.exit(1)

    # Lire les positions
    data = []
    with open(lcFileTxtName, 'r') as f:
        for line in f:
            try:
                tuple_from_line = ast.literal_eval(line.strip())
                data.append(tuple_from_line)
            except SyntaxError:
                print(f'Erreur de syntaxe dans la ligne : {line}')

    # Placer les symboles
    PlaceSymbolesOnMQchart(symbols_list)
