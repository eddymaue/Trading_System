# C:\MesOutils\Trading_System\src\db_manager.py

import sqlite3
from contextlib import contextmanager
import sys
import os

# Ajouter le répertoire racine au path pour pouvoir importer config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.db_config import DB_PATH

def init_db():
    """Initialise la base de données avec les tables nécessaires"""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Créer la table pour les données de trading (exemple)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS trading_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            symbol TEXT NOT NULL,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Vous pouvez ajouter d'autres tables ici
        
        conn.commit()
        print(f"Base de données initialisée à : {DB_PATH}")

@contextmanager
def get_connection():
    """Gère la connexion à la base de données de manière sécurisée"""
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # Pour accéder aux colonnes par nom
        yield conn
    finally:
        if conn:
            conn.close()

def get_db_version():
    """Retourne la version de SQLite"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT sqlite_version()")
        return cursor.fetchone()[0]

if __name__ == "__main__":
    # Si exécuté directement, initialiser la base de données
    print(f"Version SQLite: {get_db_version()}")
    init_db()