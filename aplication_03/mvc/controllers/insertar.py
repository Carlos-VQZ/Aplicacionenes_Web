import web
import base64
from mvc.models.modelo_insertar import ModeloInsertar

render = web.template.render('mvc/views/', base='layout')

class Insertar:
    def GET(self):
        # Renderizar la página de inserción
        return render.insertar_producto()

    def POST(self):
        try:
            # Obtener datos del formulario
            data = web.input()
            nombre = data.nombre
            descripcion = data.descripcion
            precio = data.precio
            existencias = data.existencias

            # Obtener la imagen y convertirla a Base64
            imagen = data.imagen
            imagen_base64 = base64.b64encode(imagen).decode('utf-8')

            # Instanciar el modelo
            modelo_insertar = ModeloInsertar()

            # Insertar el producto
            exito_insercion = modelo_insertar.insertar_producto(nombre, descripcion, precio, existencias, imagen_base64)

            if exito_insercion:
                # Si la inserción es exitosa, redirigir a la página de index
                web.seeother('/')
            else:
                return "Error al insertar el producto. Inténtalo de nuevo."

        except Exception as e:
            print(f"Error en POST de Insertar - {e}")
            return "Ups, algo salió mal."