import web
from mvc.models.modelo_detalle import ModeloDetalle

render = web.template.render('mvc/views/', base="layout")

class Detalle:
    def GET(self):
        try:
            params = web.input(producto_id=None)
            producto_id = params.producto_id

            if producto_id is not None:
                detalle_producto = ModeloDetalle.detalle(int(producto_id))
                if detalle_producto:
                    return render.detalle_productos(producto=detalle_producto)
                else:
                    return "Producto no encontrado"
            else:
                return "ID de producto no proporcionado"
        except Exception as e:
            return f"Error al obtener detalles del producto: {str(e)}"
