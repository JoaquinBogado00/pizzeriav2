from flask import Blueprint, render_template, request, redirect, url_for
from database.connection import obtener_conexion

cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/")
def home():
    conn = obtener_conexion()
    conn.row_factory = lambda cursor, row: dict(zip([col[0] for col in cursor.description], row))
    pizzas = conn.execute("SELECT * FROM productos").fetchall()
    conn.close()
    
    print(f"Pizzas encontradas: {pizzas}")
    return render_template("index.html", pizzas=pizzas)


@cliente_bp.route("/pedir", methods=["POST"])
def procesar_pedido():
    
    id_prod = request.form.get("id_producto")
    nombre_cliente = request.form.get("cliente")
    whatsapp = request.form.get("whatsapp")
    direccion = request.form.get("direccion")

    
    conn = obtener_conexion()
    cursor = conn.cursor()
   
    cursor.execute("""
        INSERT INTO pedidos (id_producto, cliente, direccion, telefono, estado) 
        VALUES (?, ?, ?, ?, 'Recibido')
    """, (id_prod, nombre_cliente, direccion, whatsapp))
    
    conn.commit()
    conn.close()

    
    print(f" Pedido guardado para: {nombre_cliente}")
    return redirect(url_for('cliente.home'))