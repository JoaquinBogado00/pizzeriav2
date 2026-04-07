from database.connection import obtener_conexion

def cargar_datos_iniciales():
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM productos")
    cursor.execute("DELETE FROM inventario")

    pizzas = [
        ('Muzzarella Familiar', 55000, 'Clásicas'),
        ('Fugazzeta Familiar', 65000, 'Especiales'),
        ('Napolitana Familiar', 60000, 'Clásicas'),
        ('Pepperoni Familiar', 70000, 'Especiales')
    ]
    
    cursor.executemany("INSERT INTO productos (nombre, precio, categoria) VALUES (?, ?, ?)", pizzas)

    insumos = [
        ('Harina', 50.0, 10.0),
        ('Queso Muzzarella', 20.0, 5.0),
        ('Salsa de Tomate', 15.0, 3.0)
    ]
    
    cursor.executemany("INSERT INTO inventario (ingrediente, cantidad_kg, minimo_alerta) VALUES (?, ?, ?)", insumos)

    conn.commit()
    conn.close()
    print("¡Los datos se cargaron correctamente :)!")

if __name__ == "__main__":
    cargar_datos_iniciales()