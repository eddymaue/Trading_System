#
#    Ce scrypt ouvre une fenetre modal avec 2 boutons (Executer et Quitter)
#

import os
import sys
import tkinter as tk

# Créez une fenêtre factice pour obtenir la résolution de l'écran
if False:

    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    print(f"Résolution de l'écran : {screen_width} x {screen_height} pixels")

    root.quit()

# DefautlDirectory
lcRepertoirDuScript = os.path.dirname(os.path.realpath(__file__))
os.chdir(lcRepertoirDuScript )


def start_move(event):
    fenetre_modale.x = event.x
    fenetre_modale.y = event.y

def stop_move(event):
    fenetre_modale.x = None
    fenetre_modale.y = None

def do_move(event):
    dx = event.x - fenetre_modale.x
    dy = event.y - fenetre_modale.y
    x = fenetre_modale.winfo_x() + dx
    y = fenetre_modale.winfo_y() + dy
    fenetre_modale.geometry(f"+{x}+{y}")

def fermer_fenetre():
    fenetre_modale.destroy()

def executer_script():
    print("execution de MousePutSymbol4Chart.txt")
    chemin_fichier = ".\\MouseRecorderData\\MousePutSymbol4Chart.txt"
    print(f"chemin: {chemin_fichier }")

    liFenetreDeConfirmation = "1"  #0 pour ne pas afficher

    liClickPositionOriginal = "0"  # si 1 click sur la position d'origine

    os.system(f'python MouseAutomation.py {chemin_fichier} {liFenetreDeConfirmation} {liClickPositionOriginal}') # ouvre une fentre de confirmation si 1


# Fonction pour fermer la fenêtre
# Création de la fenêtre principale
fenetre_modale = tk.Tk()

# Suppression de la barre de titres
fenetre_modale.overrideredirect(True)

# Garder la fenêtre au-dessus des autres
fenetre_modale.attributes('-topmost', True)
# Ajout d'une bordure
fenetre_modale.config(borderwidth=2, relief="solid")
# Positionnement de la fenêtre

if len(sys.argv) != 3 :
    print("Usage: python mon_script.py <left_value> <top_value>")
    topValue = 100  # Remplacez par la valeur que vous obtenez d'Excel
    leftValue = 100  # Remplacez par la valeur que vous obtenez d'Excel
else:
    try:
        # Remplacez la virgule par un point pour les valeurs décimales
        leftValue = int(sys.argv[1])

        topValue = int(sys.argv[2])

    except ValueError:
        print("Les valeurs doivent être des nombres décimaux valides.")
        sys.exit(1)


fenetre_modale.geometry(f"+{leftValue}+{topValue}")

# Création du label
label = tk.Label(fenetre_modale, text="Placez les symboles\nsélectionnés sur l'interface.")
label.pack(fill=tk.BOTH, expand=True)

# Liaison des événements de la souris aux fonctions appropriées
label.bind("<ButtonPress-1>", start_move)
label.bind("<ButtonRelease-1>", stop_move)
label.bind("<B1-Motion>", do_move)

# Création d'un cadre pour les boutons
cadre_boutons = tk.Frame(fenetre_modale)
cadre_boutons.pack()

# Création des boutons
bouton_executer = tk.Button(cadre_boutons, text="Exécuter", command=executer_script)
bouton_executer.pack(side=tk.LEFT)

# Ajout d'un espace entre les boutons
espace = tk.Label(cadre_boutons, text=" ")
espace.pack(side=tk.LEFT)

bouton_fermer = tk.Button(cadre_boutons, text="Fermer", command=fermer_fenetre)
bouton_fermer.pack(side=tk.RIGHT)

# Démarrage de la boucle principale
fenetre_modale.mainloop()
