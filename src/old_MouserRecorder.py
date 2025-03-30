import tkinter as tk
from tkinter import messagebox
from pynput import mouse, keyboard
import os
import sys

lcRepertoirDuScript = os.path.dirname(os.path.realpath(__file__))
os.chdir(lcRepertoirDuScript )

# Créer un fichier pour enregistrer les positions de la souris
try:
    file_name = sys.argv[1] #"MouseRecorder.txt"
except IndexError:
    file_name = ".\\MouseRecorderData\\MousePutSymbol4ChartQT.txt"



file = open(file_name, "w")

# Créer une fenêtre tkinter
root = tk.Tk()
root.title("Enregistreur de position de la souris")

# Créer un widget Text pour afficher les positions de la souris
text_widget = tk.Text(root)
text_widget.pack()

def on_space_pressed(x, y, button, pressed):
    if pressed:
        # Enregistrer la position de la souris dans le fichier et l'afficher dans le widget Text
        position = f"({x}, {y})\n"
        file.write(position)
        text_widget.insert(tk.END, position)

# Définir un listener de souris
mouse_listener = mouse.Listener(on_click=on_space_pressed)

# Définir un listener de clavier
keyboard_listener = keyboard.GlobalHotKeys({
    '<space>': on_space_pressed,
})

# Démarrer les listeners
mouse_listener.start()
keyboard_listener.start()

def on_accept():
    # Fermer le fichier et ouvrir le fichier avec l'application par défaut
    file.close()
    os.startfile(file_name)
    root.quit()

def on_cancel():
    # Fermer et supprimer le fichier, puis quitter l'application
    file.close()
    os.remove(file_name)
    root.quit()

# Créer des boutons Accepter et Annuler
accept_button = tk.Button(root, text="Accepter", command=on_accept)
cancel_button = tk.Button(root, text="Annuler", command=on_cancel)
accept_button.pack()
cancel_button.pack()

# Démarrer la boucle tkinter
root.mainloop()
