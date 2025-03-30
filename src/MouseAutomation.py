# MouseAutomation est un script qui déplace la souris sur des positions prédéfinies dans un fichier.txt
# Dans Excel je procede comme suivant:
#    ' Chemin vers l'interpréteur Python (changez-le si nécessaire)
#    pythonPath = "C:\Users\eddym\PycharmProjects\pythonProject\venv\Scripts\python.exe"

#    ' Chemin vers votre script Python
#    scriptPath = "C:\Users\eddym\PycharmProjects\pythonProject\BoursePlacerSurGraphiqueListeSymbolFromClipBoard\frmPlacerSymboles_v2.py"

#    Shell pythonPath & " " & scriptPath & " " & leftValue & " " & topValue ', vbNormalFocus

# Dans Python :
#    import os
#    lcRepertoirDuScript = os.path.dirname(os.path.realpath(__file__))
    # place ce fichier dans le rétoire courant ou il se situe
#    os.chdir(lcRepertoirDuScript )

    #ici j'exécute un script
#    print(os.system('python MouserRecorder.py {lcTextFile}'))




import pyautogui
import pyperclip
import time
import tkinter as tk
from tkinter import messagebox
import sys
import ast
import os

lTest = True
# DefautlDirectory
lcRepertoirDuScript = os.path.dirname(os.path.realpath(__file__))
os.chdir(lcRepertoirDuScript )

#input("test")
# Vérifiez si le fichier existe
def executeMouseRecorder(lcTextFile):
    #print(os.get_exec_path())
    print(os.system('python MouserRecorder.py {lcTextFile}'))

# Créez une fenêtre Tkinter invisible
root = tk.Tk()
root.withdraw()
lConfirmation = 0  # aucune fenetre de confirmation
lcFileTxtName = ""


#RetValue=input("cliquer sur Enter pour poursuivre")
# Vérifiez si le fichier existe
if len(sys.argv) < 2:
    if lTest:
        lcFileTxtName = ".\\MouseRecorderData\\PlaceSymboleSurChartPrincipale.txt"
        lConfirmation = 0
    else:
        messagebox.askokcancel("Fichier non trouvé",
                               "Le script MouseAutomation.py as besoin d'un arguement: Le nom du fichier dans lequel vous voulez enregistrer les évennemts de la souris MouseActionSell.txt ou MouseActionBuy.txt ")
        sys.exit()
else:
    #print(sys.argv[1])
    #print(sys.argv[2])
    #input("test2")
    lcFileTxtName = sys.argv[1]
    lConfirmation = sys.argv[2]
    lClickPositionOriginal = sys.argv[3]



print(lcFileTxtName)
# if not os.path.exists('MouseRecorder.txt'):

if not os.path.exists(lcFileTxtName):
    # Affichez une boîte de dialogue avec les options OK et Cancel
    if messagebox.askokcancel("Fichier non trouvé", "Le fichier "+lcFileTxtName+" MouseRecorder.txt n'existe pas. Voulez-vous exécuter MouseRecorder.py pour le créer ?"):
        # Si l'utilisateur clique sur OK, exécutez le script

        executeMouseRecorder(lcFileTxtName)
    else:
        sys.exit()

data = []

#with open('MouseRecorder.txt', 'r') as f:
with open(lcFileTxtName, 'r') as f:

    for line in f:
            try:
                # Utilisez ast.literal_eval pour convertir la chaîne en tuple
                tuple_from_line = ast.literal_eval(line.strip())
                data.append(tuple_from_line)
            except SyntaxError:
                print(f'Erreur de syntaxe lors de la conversion de la ligne suivante en tuple : {line}')


def PlaceClipBoardON_Txt():

    texte = pyperclip.paste()
    # Initialiser i à 0
    i = 0
    txt = ""
    txt =[]
    for couple in data:
        # Accéder aux éléments du tuple
        # x = couple[0]
        # y = couple[1]

        x, y = couple
        # print(f"x={x} , y={y}")
        # Assurez-vous que i est dans la plage de la liste des mots
        if i < len(texte.split()): #and i<9:
            Symb = {texte.split()[i]}
            # print(f"{i+1},x={x} , y={y},Symb={Symb}")
            txt.append((f"{i + 1},x={x} , y={y},Symb={Symb}"))
        i = i + 1
       # print(txt)
    return txt

def CollerSymboleInMarketQ(x , y , Symb):
    # position d'origine de la souris


   # Déplacez la souris vers le textbox (remplacez (x, y) par les coordonnées du textbox)
   # x=1531
   # y=167
    if "-TC" in Symb or "-VC" in Symb:
        # Add your code here
        pass
    elif "-U" not in Symb:
        Symb += "" #"-U"

    pyperclip.copy(Symb)
    pyautogui.moveTo(x, y)

    # Cliquez pour activer le textbox
    pyautogui.click()

    # Attendez un instant pour que le textbox soit prêt
    #time.sleep(0.01 )

    # Collez le contenu du presse-papiers
    pyautogui.hotkey('ctrl', 'v')

    # Appuyez sur Entrée
    pyautogui.press('enter')

# noinspection PyPep8
def PlaceClipBoardON_MQchart():

    global lClickPositionOriginal

    texte = pyperclip.paste()
    # Initialiser i à 0
    i = 0
    txt = ""
    txt = []
    mX, mY = pyautogui.position()
    for couple in data:
        # Accéder aux éléments du tuple
        # x = couple[0]
        # y = couple[1]

        x, y = couple
        # print(f"x={x} , y={y}")
        # Assurez-vous que i est dans la plage de la liste des mots
        if i < len(texte.split()) : #and i < 9:
            Symb = texte.split()[i]
            # print(f"{i+1},x={x} , y={y},Symb={Symb}")
            #print(x,y,Symb, sep=', ')
            CollerSymboleInMarketQ(x,y,Symb)

        i = i + 1


    pyautogui.moveTo(mX, mY)
    if lClickPositionOriginal == 1:
        pyautogui.click()


    return txt

def create_confirmation_window():
    global lConfirmation
    window = tk.Tk()
    window.withdraw()  # Cacher la fenêtre principale

    # Convertir la liste en une chaîne
    data_str = "\n".join(PlaceClipBoardON_Txt())

    # Créer une boîte de dialogue de confirmation

    if isinstance(lConfirmation, str):
        lConfirmation = int(lConfirmation)

    if lConfirmation == 1:
        result = messagebox.askokcancel("Confirmation",data_str)
    else:
        result = True

    if result:
        PlaceClipBoardON_MQchart()
        print("Vous avez cliqué sur OK")
    else:
        print("Vous avez cliqué sur Cancel")

    window.destroy()

create_confirmation_window()
