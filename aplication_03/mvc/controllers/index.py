import web
from mvc.models.modelo_index import ModeloIndex

render = web.template.render('mvc/views/', base='layout')
modelo_index = ModeloIndex()

class Index:
    def GET(self):
        try:
            # Obtener parámetros de la URL
            params = web.input(page=1, items_per_page=9)
            page = int(params.page)
            items_per_page = int(params.items_per_page)

            # Obtener productos para la página actual
            datos = modelo_index.obtener_productos_paginados(page, items_per_page)

            # Obtener el total de productos para calcular el número total de páginas
            total_productos = modelo_index.obtener_total_productos()
            total_pages = (total_productos + items_per_page - 1) // items_per_page

            return render.index(datos=datos, page=page, total_pages=total_pages)
        except Exception as e:
            print(f"Error al obtener productos: {e}")
            return "Lo siento, algo salió mal al obtener los productos."

    def POST(self):
        try:
            data = web.input(query=None)
            query = data.query

            if query:
                # Buscar productos
                page = 1
                items_per_page = 9
                resultados = modelo_index.buscar_productos(query)
                
                return render.index(datos=resultados, page=page, total_pages=1)
            else:
                return web.seeother('/')

        except Exception as e:
            print(f"Error al realizar la búsqueda: {e}")
            return "Lo siento, algo salió mal durante la búsqueda."
