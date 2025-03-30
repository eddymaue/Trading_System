import keyboard
import time
import os
from datetime import datetime

lcRepertoirDuScript = os.path.dirname(os.path.realpath(__file__))
os.chdir(lcRepertoirDuScript )

def executer_script(lcTxtFil):
    os.system(f'python MouseAutomation.py {lcTxtFil}')

def MouseActionBuy_by_FN_F9():
    if IsRegularHours():
        # print("nous somme en inside hours")
        lcTextFile = ".\\MouseRecorderData\\MouseBuyRegHrs.txt"

    else:
        # print("nous somme en Extend hours")
        lcTextFile = ".\\MouseRecorderData\\MouseBuyExtHrs.txt"

    executer_script(lcTextFile)
    IsKeyPressed("F9")


def MouseActionSell_by_FN_F12():

     if IsRegularHours():
        # print("nous somme en inside hours")
        lcTextFile = ".\\MouseRecorderData\\MouseSellRegHrs.txt"

     else:
        # print("nous somme en Extend hours")
        lcTextFile = ".\\MouseRecorderData\\MouseSellExtHrs.txt"

     executer_script(lcTextFile)

     # empache la répétition de la touche pressée.
     IsKeyPressed("F12")

def IsKeyPressed(lcKey):
    while keyboard.is_pressed(lcKey):
        i=1

def IsRegularHours():
    # Obtenir l'heure actuelle
    maintenant =   datetime.now().time()

    # Définir les heures de début et de fin
    heure_debut = datetime.strptime("9:30", "%H:%M").time()
    heure_fin = datetime.strptime("16:00", "%H:%M").time()

    # cette condition vérifie si maintenant est entre heure_debut et heure_fin,
    # inclusivement. Si c’est le cas, la condition est vraie. Sinon, elle est fausse. 😊
    #print(heure_debut <= maintenant  <= heure_fin)
    return  heure_debut <= maintenant  <= heure_fin


while True:
    if keyboard.is_pressed('F9'):
        #print(" MouseActionBuyF9()")
        MouseActionBuy_by_FN_F9()

    elif keyboard.is_pressed('F12'):
        MouseActionSell_by_FN_F12()

    time.sleep(0.1)  # pause de 200 ms