# C:\MesOutils\Trading_System\src\data_importer.py

import os
import sys
import pandas as pd
from datetime import datetime

# Ajouter le répertoire racine au path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.db_manager import get_connection

def import_excel_data(excel_file_path, symbol):
    """Importe des données depuis un fichier Excel vers la base de données"""
    try:
        # Lire le fichier Excel
        df = pd.read_excel(excel_file_path)
        
        # Vérifier les colonnes nécessaires
        required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"Colonnes manquantes dans le fichier Excel: {missing_columns}")
            return False
        
        # Convertir les données et insérer dans la base de données
        with get_connection() as conn:
            cursor = conn.cursor()
            
            # Préparer les données à insérer
            data_to_insert = []
            for _, row in df.iterrows():
                date_str = row['Date']
                # Convertir la date si nécessaire
                if isinstance(date_str, datetime):
                    date_str = date_str.strftime('%Y-%m-%d')
                
                data_to_insert.append((
                    date_str,
                    symbol,
                    float(row['Open']),
                    float(row['High']),
                    float(row['Low']),
                    float(row['Close']),
                    int(row['Volume'])
                ))
            
            # Insérer les données
            cursor.executemany('''
            INSERT INTO trading_data (date, symbol, open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', data_to_insert)
            
            conn.commit()
            print(f"Importé {len(data_to_insert)} lignes pour {symbol}")
            return True
    
    except Exception as e:
        print(f"Erreur lors de l'importation des données: {e}")
        return False

if __name__ == "__main__":
    # Exemple d'utilisation
    excel_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'excel'))
    
    # Vérifiez si des fichiers Excel existent
    excel_files = [f for f in os.listdir(excel_dir) if f.endswith('.xlsx')]
    
    if not excel_files:
        print(f"Aucun fichier Excel trouvé dans {excel_dir}")
    else:
        # Importer le premier fichier comme exemple
        sample_file = os.path.join(excel_dir, excel_files[0])
        symbol = os.path.splitext(excel_files[0])[0].upper()
        
        print(f"Importation du fichier {sample_file} pour le symbole {symbol}")
        import_excel_data(sample_file, symbol)