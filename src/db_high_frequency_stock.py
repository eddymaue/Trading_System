import sqlite3
from datetime import datetime
import pandas as pd

class HighFrequencyStockDB:
    def __init__(self, db_path="high_frequency_stock_data.db"):
        """Initialise la connexion à la base de données."""
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row  # Pour pouvoir accéder aux colonnes par leur nom
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        """Crée les tables si elles n'existent pas."""
        # Table pour les tickers (symboles des actions)
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickers (
            ticker_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT UNIQUE
        )
        ''')
        
        # Table pour l'historique des prix (sans contrainte d'unicité sur timestamp)
        # Cela permet d'avoir plusieurs entrées pour le même ticker à la même minute/seconde
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker_id INTEGER,
            timestamp DATETIME,
            price REAL,
            volume INTEGER,
            FOREIGN KEY (ticker_id) REFERENCES tickers(ticker_id)
        )
        ''')
        
        # Création d'un index pour optimiser les requêtes par ticker et timestamp
        self.cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_ticker_timestamp 
        ON price_history (ticker_id, timestamp)
        ''')
        
        self.conn.commit()
    
    def get_or_create_ticker(self, ticker_symbol):
        """Récupère l'ID du ticker ou le crée s'il n'existe pas."""
        self.cursor.execute("SELECT ticker_id FROM tickers WHERE ticker = ?", (ticker_symbol,))
        result = self.cursor.fetchone()
        
        if result:
            return result[0]
        else:
            self.cursor.execute("INSERT INTO tickers (ticker) VALUES (?)", (ticker_symbol,))
            self.conn.commit()
            return self.cursor.lastrowid
    
    # Opérations CRUD pour les données de prix
    
    def add_price_data(self, ticker_symbol, timestamp, price, volume):
        """Ajoute une nouvelle entrée de prix pour un ticker.
        Cette fonction permet d'ajouter plusieurs entrées à la même minute/seconde."""
        ticker_id = self.get_or_create_ticker(ticker_symbol)
        
        try:
            self.cursor.execute('''
            INSERT INTO price_history (ticker_id, timestamp, price, volume)
            VALUES (?, ?, ?, ?)
            ''', (ticker_id, timestamp, price, volume))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erreur lors de l'ajout des données: {e}")
            return False
    
    def get_price_data(self, ticker_symbol, start_date=None, end_date=None):
        """Récupère les données de prix pour un ticker sur une période donnée."""
        ticker_id = self.get_or_create_ticker(ticker_symbol)
        
        query = '''
        SELECT ph.id, t.ticker, ph.timestamp, ph.price, ph.volume
        FROM price_history ph
        JOIN tickers t ON ph.ticker_id = t.ticker_id
        WHERE t.ticker_id = ?
        '''
        params = [ticker_id]
        
        if start_date:
            query += " AND ph.timestamp >= ?"
            params.append(start_date)
        
        if end_date:
            query += " AND ph.timestamp <= ?"
            params.append(end_date)
        
        query += " ORDER BY ph.timestamp ASC"
        
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def update_price_data(self, data_id, price=None, volume=None):
        """Met à jour les données de prix pour une entrée spécifique par son ID."""
        # Construire la requête de mise à jour en fonction des paramètres fournis
        query = "UPDATE price_history SET "
        params = []
        
        if price is not None:
            query += "price = ?"
            params.append(price)
        
        if volume is not None:
            if price is not None:
                query += ", "
            query += "volume = ?"
            params.append(volume)
        
        if not params:
            return False  # Rien à mettre à jour
        
        query += " WHERE id = ?"
        params.append(data_id)
        
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def delete_price_data_by_id(self, data_id):
        """Supprime une entrée spécifique par son ID."""
        self.cursor.execute("DELETE FROM price_history WHERE id = ?", (data_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def delete_price_data(self, ticker_symbol, start_date=None, end_date=None):
        """Supprime les données de prix pour un ticker, éventuellement sur une période spécifique."""
        ticker_id = self.get_or_create_ticker(ticker_symbol)
        
        if start_date and end_date:
            # Supprime les entrées dans la période spécifiée
            self.cursor.execute('''
            DELETE FROM price_history 
            WHERE ticker_id = ? AND timestamp >= ? AND timestamp <= ?
            ''', (ticker_id, start_date, end_date))
        elif start_date:
            # Supprime les entrées à partir de la date de début
            self.cursor.execute('''
            DELETE FROM price_history 
            WHERE ticker_id = ? AND timestamp >= ?
            ''', (ticker_id, start_date))
        elif end_date:
            # Supprime les entrées jusqu'à la date de fin
            self.cursor.execute('''
            DELETE FROM price_history 
            WHERE ticker_id = ? AND timestamp <= ?
            ''', (ticker_id, end_date))
        else:
            # Supprime toutes les entrées pour ce ticker
            self.cursor.execute("DELETE FROM price_history WHERE ticker_id = ?", (ticker_id,))
        
        self.conn.commit()
        return self.cursor.rowcount
    
    def get_data_as_dataframe(self, ticker_symbol, start_date=None, end_date=None):
        """Récupère les données sous forme de DataFrame pandas."""
        rows = self.get_price_data(ticker_symbol, start_date, end_date)
        if not rows:
            return pd.DataFrame()
        
        # Convertir les résultats en dictionnaire pour pandas
        data = []
        for row in rows:
            data.append(dict(row))
        
        return pd.DataFrame(data)
    
    def import_from_dataframe(self, df, ticker_column='ticker', timestamp_column='timestamp', 
                             price_column='price', volume_column='volume'):
        """Importe des données depuis un DataFrame pandas."""
        success_count = 0
        for _, row in df.iterrows():
            result = self.add_price_data(
                row[ticker_column], 
                row[timestamp_column], 
                row[price_column], 
                row[volume_column]
            )
            if result:
                success_count += 1
        
        return success_count
        
    def get_aggregate_by_minute(self, ticker_symbol, start_date=None, end_date=None):
        """Récupère les données agrégées par minute (OHLC - Open, High, Low, Close).
        Utile pour convertir des données à haute fréquence en données à la minute."""
        ticker_id = self.get_or_create_ticker(ticker_symbol)
        
        # Formater le timestamp pour regrouper par minute
        # Cette fonction SQL extrait la date et l'heure jusqu'à la minute
        query = '''
        SELECT 
            t.ticker,
            strftime('%Y-%m-%d %H:%M:00', ph.timestamp) as minute,
            MIN(ph.price) as low_price,
            MAX(ph.price) as high_price,
            FIRST_VALUE(ph.price) OVER (PARTITION BY strftime('%Y-%m-%d %H:%M:00', ph.timestamp) ORDER BY ph.timestamp) as open_price,
            LAST_VALUE(ph.price) OVER (PARTITION BY strftime('%Y-%m-%d %H:%M:00', ph.timestamp) ORDER BY ph.timestamp) as close_price,
            SUM(ph.volume) as total_volume,
            COUNT(*) as num_trades
        FROM price_history ph
        JOIN tickers t ON ph.ticker_id = t.ticker_id
        WHERE t.ticker_id = ?
        '''
        params = [ticker_id]
        
        if start_date:
            query += " AND ph.timestamp >= ?"
            params.append(start_date)
        
        if end_date:
            query += " AND ph.timestamp <= ?"
            params.append(end_date)
        
        query += " GROUP BY t.ticker, minute ORDER BY minute ASC"
        
        try:
            self.cursor.execute(query, params)
            rows = self.cursor.fetchall()
            
            # Convertir les résultats en dictionnaire pour pandas
            data = []
            for row in rows:
                data.append(dict(row))
            
            return pd.DataFrame(data)
        except sqlite3.Error as e:
            # Si votre version de SQLite ne prend pas en charge FIRST_VALUE/LAST_VALUE
            # on utilisera une approche alternative
            print(f"Erreur lors de l'agrégation: {e}")
            return self._fallback_aggregate_by_minute(ticker_symbol, start_date, end_date)
    
    def _fallback_aggregate_by_minute(self, ticker_symbol, start_date=None, end_date=None):
        """Méthode alternative pour l'agrégation par minute si les fonctions window ne sont pas disponibles."""
        # Récupérer toutes les données d'abord
        df = self.get_data_as_dataframe(ticker_symbol, start_date, end_date)
        if df.empty:
            return pd.DataFrame()
        
        # Convertir le timestamp en datetime si ce n'est pas déjà fait
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Créer une colonne de minute pour le regroupement
        df['minute'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:00')
        
        # Grouper et agréger
        aggregated = df.groupby(['ticker', 'minute']).agg(
            open_price=('price', 'first'),
            high_price=('price', 'max'),
            low_price=('price', 'min'),
            close_price=('price', 'last'),
            total_volume=('volume', 'sum'),
            num_trades=('id', 'count')
        ).reset_index()
        
        return aggregated
    
    def close(self):
        """Ferme la connexion à la base de données."""
        self.conn.close()


# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance de la base de données
    db = HighFrequencyStockDB("high_freq_stocks.db")
    
    # Ajout de quelques données d'exemple au niveau 15 secondes
    current_time = "2023-01-01 12:00:00"
    db.add_price_data("AAPL", current_time, 175.25, 1200)
    
    current_time = "2023-01-01 12:00:15"
    db.add_price_data("AAPL", current_time, 175.30, 800)
    
    current_time = "2023-01-01 12:00:30"
    db.add_price_data("AAPL", current_time, 175.27, 950)
    
    current_time = "2023-01-01 12:00:45"
    db.add_price_data("AAPL", current_time, 175.32, 1100)
    
    current_time = "2023-01-01 12:01:00"
    db.add_price_data("AAPL", current_time, 175.35, 1300)
    
    # Lecture des données brutes
    apple_data = db.get_price_data("AAPL")
    print("Données Apple au niveau 15 secondes:")
    for row in apple_data:
        print(dict(row))
    
    # Obtenir les données agrégées par minute
    agg_data = db.get_aggregate_by_minute("AAPL")
    print("\nDonnées Apple agrégées par minute (OHLC):")
    print(agg_data)
    
    # Fermeture de la connexion
    db.close()