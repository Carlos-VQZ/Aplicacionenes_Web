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
            conn = sqlite3.connect('productos.db')  # Crear una nueva conexión en cada llamada
            cursor = conn.cursor()

            # Realiza una búsqueda en la base de datos según el query
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ? OR descripcion LIKE ?",
                        ('%' + query + '%', '%' + query + '%'))

            resultados = cursor.fetchall()

            conn.close()
            return resultados
        except Exception as e:
            print(f"Error en la búsqueda: {e}")
            return []  # Devuelve una lista vacía en caso de error

    def obtener_total_productos(self):
        try:
            conn = sqlite3.connect('productos.db')
            cursor = conn.cursor()

            # Consulta SQL para obtener el total de productos
            cursor.execute("SELECT COUNT(*) FROM productos")

            total_productos = cursor.fetchone()[0]

            conn.close()
            return total_productos
        except Exception as e:
            print(f"Error al obtener el total de productos: {e}")
            return 0

    def obtener_productos_paginados(self, page, items_per_page):
        try:
            conn = sqlite3.connect('productos.db')
            cursor = conn.cursor()

            offset = (page - 1) * items_per_page

            # Consulta SQL para obtener productos paginados
            query = f"SELECT * FROM productos LIMIT {items_per_page} OFFSET {offset}"
            cursor.execute(query)

            productos = cursor.fetchall()

            conn.close()
            return productos
        except Exception as e:
            print(f"Error al obtener productos paginados: {e}")
            return None