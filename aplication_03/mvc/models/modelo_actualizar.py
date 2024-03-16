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

    def actualizar_producto(self, id_producto, nombre, descripcion, precio, existencias, imagen_base64):
        try:
            # Establecer conexión a la base de datos
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Define la consulta SQL para la actualización
            consulta = "UPDATE productos SET nombre=?, descripcion=?, precio=?, existencias=?, imagen=? WHERE id=?"
            
            # Ejecuta la consulta con los valores actualizados
            datos_producto = (nombre, descripcion, precio, existencias, imagen_base64, id_producto)
            cursor.execute(consulta, datos_producto)
            
            # Guarda los cambios
            conn.commit()
            
            # Cierra la conexión
            conn.close()
            
            # Indica que la actualización fue exitosa
            return True
        except Exception as e:
            print(f"Error al actualizar producto - {e}")
            return False

class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, existencias, imagen_base64):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
        self.imagen_base64 = imagen_base64
