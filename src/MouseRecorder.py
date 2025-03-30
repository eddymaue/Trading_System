import tkinter as tk
import pyautogui
import os
import sys
from pathlib import Path

# Obtenir le répertoire du script de manière plus robuste
SCRIPT_DIR = Path(__file__).parent.absolute()
DATA_DIR = SCRIPT_DIR / "MouseRecorderData"

# Créer le répertoire de données s'il n'existe pas
DATA_DIR.mkdir(exist_ok=True)

# Gestion du nom de fichier par défaut
try:
    file_name = sys.argv[1]
except IndexError:
    file_name = DATA_DIR / "MousePutSymbo16ChartTradingView.txt"

class MouseRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Enregistreur de position de la souris")
        
        # Configuration de la fenêtre
        self.root.geometry("400x300")
        
        # Création des widgets
        self.create_widgets()
        
        # Ouverture du fichier
        self.file = open(file_name, "w", encoding="utf-8")
        
    def create_widgets(self):
        # Zone de texte avec scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text_widget = tk.Text(self.frame, yscrollcommand=self.scrollbar.set)
        self.text_widget.pack(fill=tk.BOTH, expand=True)
        
        self.scrollbar.config(command=self.text_widget.yview)
        
        # Boutons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.accept_button = tk.Button(self.button_frame, text="Accepter", command=self.on_accept)
        self.accept_button.pack(side=tk.LEFT, padx=5)
        
        self.cancel_button = tk.Button(self.button_frame, text="Annuler", command=self.on_cancel)
        self.cancel_button.pack(side=tk.LEFT)
        
        # Label d'instructions
        self.instructions = tk.Label(self.root, 
                                   text="Appuyez sur ESPACE pour enregistrer la position\nde la souris",
                                   justify=tk.CENTER)
        self.instructions.pack(pady=5)
        
        # Binding des événements
        self.root.bind('<space>', self.on_space_pressed)
        
    def on_space_pressed(self, event):
        try:
            x, y = pyautogui.position()
            position = f"({x}, {y})\n"
            self.file.write(position)
            self.text_widget.insert(tk.END, position)
            self.text_widget.see(tk.END)  # Auto-scroll
        except Exception as e:
            self.text_widget.insert(tk.END, f"Erreur: {str(e)}\n")
    
    def on_accept(self):
        try:
            self.file.close()
            os.startfile(str(file_name))  # Conversion en str pour compatibilité
        except Exception as e:
            print(f"Erreur lors de l'ouverture du fichier: {str(e)}")
        finally:
            self.root.quit()
    
    def on_cancel(self):
        self.file.close()
        try:
            os.remove(file_name)
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier: {str(e)}")
        finally:
            self.root.quit()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MouseRecorder()
    app.run()