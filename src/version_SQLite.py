import sqlite3
print(f"Version de SQLite: {sqlite3.sqlite_version}")

# Si vous voulez utiliser SQLAlchemy avec SQLite
from sqlalchemy import create_engine, text
engine = create_engine('sqlite:///:memory:')
with engine.connect() as conn:
    result = conn.execute(text("SELECT sqlite_version()"))
    print(f"Version de SQLite via SQLAlchemy: {result.scalar()}")