import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR,"..", "pizzeria.db")

def obtener_conexion():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_db():
    conn = obtener_conexion()
    schema_path = os.path.join(BASE_DIR, "schema.sql")
    with open(schema_path, 'r') as f:
        conn.executescript(f.read())
    conn.close()
    print("base de datos iniciada correctamente")





