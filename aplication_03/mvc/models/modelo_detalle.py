import sqlite3

class ModeloDetalle:
    def __init__(self, id_producto, nombre, descripcion, precio, existencias):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias

    @classmethod
    def detalle(cls, id_producto):
        try:
            conexion = sqlite3.connect('productos.db')
            cursor = conexion.cursor()

            cursor.execute("SELECT * FROM productos WHERE id=?", (id_producto,))
            producto_data = cursor.fetchone()

            conexion.close()

            if producto_data:
                producto = cls(*producto_data)  # Utiliza el desempaquetado para pasar todos los datos
                return producto
            else:
                return None
        except Exception as e:
            print(f"Error al obtener producto por ID: {str(e)}")
            return None
