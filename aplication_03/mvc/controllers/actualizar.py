import web
from mvc.models.modelo_actualizar import ModeloActualizar

render = web.template.render('mvc/views/', base='layout')
m_actualizar = ModeloActualizar()

class Actualizar:
    def GET(self):
        try:
            params = web.input(producto_id=None)
            id_producto = params.producto_id

            print(f"URL: {web.ctx.fullpath}")
            print(f"id_producto: {id_producto}")

            if not id_producto:
                return "Debe proporcionar el ID del producto a actualizar."

            # Obtener el producto por ID
            producto = m_actualizar.obtener_producto_por_id(int(id_producto))

            if producto:
                return render.actualizar_producto(producto=producto)
            else:
                return "Producto no encontrado."
        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."

    def POST(self):
        try:
            data = web.input(id_producto=None, nombre=None, descripcion=None, precio=None, existencias=None)
            id_producto = data.id_producto

            if not id_producto:
                return "Debe proporcionar el ID del producto a actualizar."

            # Obtener datos actualizados del formulario
            nombre = data.nombre
            descripcion = data.descripcion
            precio = data.precio
            existencias = data.existencias

            # Actualizar el producto por ID
            m_actualizar.actualizar_producto(int(id_producto), nombre, descripcion, precio, existencias)
            raise web.seeother('/')

        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."
