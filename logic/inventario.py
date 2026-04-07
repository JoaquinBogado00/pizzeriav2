from database.connection import obtener_conexion

def descontar_insumos(id_producto):
    conn = obtener_conexion()
    receta = conn.execute("""
SELECT id_insumo, cantidad_necesaria FROM recetas WHERE id_producto = ?,""", (id_producto,)).fetchall()
    
    for item in receta:
        conn.execute("""
        UPDATE inventario
        SET cantidad_kg = cantidad_kg - ?
        WHERE id = ?""", (item["cantidad_necesaria"], item["id_insumo"]))

    conn.commit()
    conn.close()
    