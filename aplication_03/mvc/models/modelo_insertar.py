import sqlite3
import web

render = web.template.render('mvc/views/', base='layout')

class ModeloInsertar:
    def __init__(self):
        # Conéctate a la base de datos al instanciar el modelo
        self.connection = sqlite3.connect('productos.db')
        self.cursor = self.connection.cursor()

    def insertar_producto(self, nombre, descripcion, precio, existencias):
        try:
            # Define la consulta SQL para la inserción (ajusta según tu tabla)
            consulta = "INSERT INTO productos (nombre, descripcion, precio, existencias) VALUES (?, ?, ?, ?)"

            # Ejecuta la consulta con los valores del formulario
            datos_producto = (nombre, descripcion, precio, existencias)
            self.cursor.execute(consulta, datos_producto)

            # Guarda los cambios
            self.connection.commit()

            # Indica que la inserción fue exitosa
            return True
        except Exception as e:
            print(f"Error al insertar producto - {e}")
            return False
