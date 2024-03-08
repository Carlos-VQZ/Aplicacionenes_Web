import web
from mvc.models.modelo_borrar import ModeloBorrar

render = web.template.render('mvc/views/', base='layout')
m_borrar = ModeloBorrar()

class Borrar:
    def GET(self):
        try:
            params = web.input(producto_id=None)
            id_producto = params.producto_id

            print(f"URL: {web.ctx.fullpath}")
            print(f"id_producto: {id_producto}")

            if not id_producto:
                return "Debe proporcionar el ID del producto."

            # Obtener el producto por ID
            producto = m_borrar.obtener_producto_por_id(int(id_producto))

            if producto:
                return render.borrar_productos(producto=producto)
            else:
                return "Producto no encontrado."
        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."

    def POST(self):
        try:
            data = web.input(id_producto=None)
            id_producto = data.id_producto

            if not id_producto:
                return "Debe proporcionar el ID del producto a borrar."

            # Borrar el producto por ID
            m_borrar.borrar_producto_por_id(int(id_producto))
            raise web.seeother('/')

        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."
