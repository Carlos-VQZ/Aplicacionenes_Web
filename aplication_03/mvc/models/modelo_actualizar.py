import sqlite3

class ModeloActualizar:
    def __init__(self):
        self.db_name = 'productos.db'

    def obtener_producto_por_id(self, id_producto):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM productos WHERE id=?", (id_producto,))
        producto = c.fetchone()
        conn.close()

        if producto:
            return Producto(*producto)
        else:
            return None

    def actualizar_producto(self, id_producto, nombre, descripcion, precio, existencias):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("UPDATE productos SET nombre=?, descripcion=?, precio=?, existencias=? WHERE id=?",
                  (nombre, descripcion, precio, existencias, id_producto))
        conn.commit()
        conn.close()

class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, existencias):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
