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
  
        #print(symbols_list)

        if i < len(symbols_list):
            Symb = symbols_list[i]
            # Ajouter -U si nécessaire
            #if "-TC" not in Symb and "-VC" not in Symb and "-U" not in Symb:
            #    Symb += "" #"-U"

            # Déplacer et cliquer
            pyautogui.moveTo(x, y)
            pyautogui.click()
            #pyautogui.click()
            #pyautogui.hotkey('space')

            # Taper directement le symbole
            pyautogui.typewrite(Symb)
            time.sleep(0.5)

            #print(Symb)
            #pyperclip.copy(Symb)
	    
	    # Collez le contenu du presse-papiers
            #pyautogui.hotkey('ctrl', 'v')


            pyautogui.press('enter')
       	    time.sleep(0.5)
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