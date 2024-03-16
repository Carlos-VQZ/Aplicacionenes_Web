import web
import base64
from mvc.models.modelo_actualizar import ModeloActualizar

render = web.template.render('mvc/views/', base='layout')

class Actualizar:
    def GET(self):
        try:
            # Obtener el ID del producto de la URL
            params = web.input(producto_id=None)
            id_producto = params.producto_id

            if not id_producto:
                return "Debe proporcionar el ID del producto a actualizar."

            # Obtener el producto por ID
            modelo_actualizar = ModeloActualizar()
            producto = modelo_actualizar.obtener_producto_por_id(int(id_producto))

            if producto:
                # Renderizar el formulario de actualización con los datos del producto
                return render.actualizar_producto(producto=producto)
            else:
                return "Producto no encontrado."

        except Exception as e:
            print(f"Error en GET de Actualizar - {e}")
            return "Ups, algo salió mal."
            
    def POST(self):
        try:
            # Obtener datos del formulario de actualización
            data = web.input()
            id_producto = data.id_producto
            nombre = data.nombre
            descripcion = data.descripcion
            precio = data.precio
            existencias = data.existencias

            # Obtener la imagen y convertirla a Base64 si se proporciona
            imagen = data.imagen
            imagen_base64 = base64.b64encode(imagen).decode('utf-8')

            # Instanciar el modelo
            modelo_actualizar = ModeloActualizar()
            print(imagen_base64)

            # Actualizar el producto
            modelo_actualizar.actualizar_producto(int(id_producto), nombre, descripcion, precio, existencias, imagen_base64)

            # Renderizar la página de detalles del producto actualizado
            producto_actualizado = modelo_actualizar.obtener_producto_por_id(int(id_producto))
            return render.actualizar_producto(producto=producto_actualizado)

        except Exception as e:
            error_message = f"Error en POST de Actualizar - {e}"
            print(error_message)
            return error_message
