from flask import Blueprint, render_template, request, redirect, url_for
from database.connection import obtener_conexion

admin_bp = Blueprint("admin", __name__, template_folder='../templates')

@admin_bp.route("/", strict_slashes=False)
def panel_control():
    conn = obtener_conexion()
    conn.row_factory = lambda cursor, row: dict(zip([col[0] for col in cursor.description], row))
    
    query = """
        SELECT 
            pedidos.id, 
            pedidos.cliente, 
            pedidos.direccion, 
            pedidos.telefono, 
            pedidos.estado, 
            productos.nombre as pizza_nombre
        FROM pedidos
        JOIN productos ON pedidos.id_producto = productos.id
        ORDER BY pedidos.id DESC
    """
   

    try:
        pedidos = conn.execute(query).fetchall()
    except Exception as e:
        print(f"Error en la base de datos: {e}")
        pedidos = [] 
        
    conn.close()
    return render_template("admin.html", pedidos=pedidos)
    
   

@admin_bp.route("/admin/estado/<int:id_pedido>/<nuevo_estado>")
def actualizar_estado(id_pedido, nuevo_estado):
    conn = obtener_conexion()
    conn.execute("UPDATE pedidos SET estado = ? WHERE id = ?", (nuevo_estado, id_pedido))
    conn.commit()
    conn.close()
    return redirect(url_for('admin.panel_control'))


