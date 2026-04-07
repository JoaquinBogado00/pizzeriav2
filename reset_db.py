import sqlite3
import os

db_name = "pizzeria.db"
schema_file = "database/schema.sql"

if os.path.exists(db_name):
    os.remove(db_name)
    print(f" Archivo {db_name} borrado con éxito.")

try:
    conn = sqlite3.connect(db_name)
    with open(schema_file, "r", encoding="utf-8") as f:
        schema_sql = f.read()
    
    conn.executescript(schema_sql)
    conn.commit()
    conn.close()
    print(" Base de datos creada de nuevo con el esquema de schema.sql")
except Exception as e:
    print(f" Error al resetear: {e}")