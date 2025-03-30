# C:\MesOutils\Trading_System\src\test_db.py

import os
import sys

# Ajouter le répertoire racine au path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.db_manager import get_connection, init_db, get_db_version

def test_database():
    """Teste les fonctionnalités de base de la base de données"""
    print(f"Version SQLite: {get_db_version()}")
    
    # S'assurer que la base de données est initialisée
    init_db()
    
    # Tester une requête simple
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Compter les enregistrements dans la table trading_data
        cursor.execute("SELECT COUNT(*) FROM trading_data")
        count = cursor.fetchone()[0]
        
        print(f"Nombre d'enregistrements dans trading_data: {count}")
        
        # Afficher les 5 premiers enregistrements s'il y en a
        if count > 0:
            cursor.execute("""
            SELECT id, date, symbol, open, close, volume 
            FROM trading_data 
            ORDER BY date DESC LIMIT 5
            """)
            
            rows = cursor.fetchall()
            print("\nDernières données de trading:")
            print("ID\tDate\t\tSymbole\tOuverture\tFermeture\tVolume")
            print("-" * 70)
            
            for row in rows:
                print(f"{row['id']}\t{row['date']}\t{row['symbol']}\t{row['open']}\t{row['close']}\t{row['volume']}")

if __name__ == "__main__":
    test_database()