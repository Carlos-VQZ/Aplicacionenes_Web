import sqlite3

class ModeloIndex:
    def __init__(self):
        # Conectar a la base de datos SQLite
        self.connection = sqlite3.connect('productos.db')
        self.cursor = self.connection.cursor()

    def obtener_todos_los_productos(self):
        try:
            self.cursor.execute("SELECT * FROM productos")
            productos_data = self.cursor.fetchall()
            return productos_data
        except Exception as e:
            print(f"Error al obtener todos los productos: {str(e)}")
            return []

    def buscar_productos(self, query):
        try:
            conn = sqlite3.connect('productos.db')
            cursor = conn.cursor()

            # Realiza una búsqueda en la base de datos según el query
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ? OR descripcion LIKE ?",
                           ('%' + query + '%', '%' + query + '%'))

            resultados = cursor.fetchall()

            conn.close()
            return resultados
        except Exception as e:
            print(f"Error en la búsqueda: {e}")
            return None