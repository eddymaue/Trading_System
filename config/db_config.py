# C:\MesOutils\Trading_System\config\db_config.py

import os

# Chemin base du projet
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Chemin vers le dossier de base de données
DB_DIR = os.path.join(BASE_DIR, 'data', 'db')

# Nom du fichier de base de données
DB_NAME = 'trading_data.db'

# Chemin complet de la base de données
DB_PATH = os.path.join(DB_DIR, DB_NAME)

# Assurez-vous que le dossier db existe
os.makedirs(DB_DIR, exist_ok=True)