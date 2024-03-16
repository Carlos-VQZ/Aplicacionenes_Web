import sqlite3

class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, existencias, imagen_base64):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
        self.imagen_base64 = imagen_base64

class ModeloBorrar:
    def __init__(self):
        self.db_name = 'productos.db'

    def borrar_producto_por_id(self, id_producto):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM productos WHERE id=?", (id_producto,))
        conn.commit()
        conn.close()

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
