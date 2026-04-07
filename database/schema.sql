DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS inventario;

CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio TEXT NOT NULL,
    categoria TEXT 
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_producto INTEGER,
    cliente TEXT NOT NULL,
    direccion TEXT NOT NULL,
    telefono TEXT NOT NULL,
    estado TEXT DEFAULT 'Recibido',
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(id_producto) REFERENCES productos(id)
);;

CREATE TABLE inventario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingrediente TEXT NOT NULL,
    cantidad_kg REAL NOT NULL,
    minimo_alerta REAL NOT NULL
);

CREATE TABLE recetas (
    id_producto INTEGER,
    id_ingrediente INTEGER,
    cantidad_necesaria REAL,
    FOREIGN KEY(id_producto) REFERENCES productos(id),
    FOREIGN KEY(id_ingrediente) REFERENCES inventario(id)
);


