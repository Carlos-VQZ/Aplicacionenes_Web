import web
from mvc.models.modelo_index import ModeloIndex

render = web.template.render('mvc/views/', base='layout')

class Index:
    def GET(self):
        try:
            m_index = ModeloIndex()
            resultado = m_index.obtener_todos_los_productos()
            return render.index(datos=resultado)
        except Exception as e:
            print(f"Error 101 - index {e.args}")
            return "Ups, algo salió mal"

    def POST(self):
        try:
            m_index = ModeloIndex()
            data = web.input(query=None)
            query = data.query

            if query:
                resultados = m_index.buscar_productos(query)
                return render.index(resultados)
            else:
                return web.seeother('/')

        except Exception as e:
            print(f"Error al realizar la búsqueda: {e}")
            return "Lo siento, algo salió mal durante la búsqueda."