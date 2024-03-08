import web
from mvc.models.modelo_index import ModeloIndex

render = web.template.render('mvc/views/', base='layout')
m_index = ModeloIndex()

class Index:
    def GET(self):
        try:
            # Al cargar la página, renderizas el formulario sin resultados
            return render.index(datos=None, num1=None, num2=None)
        except Exception as e:
            print(f"Error 101 - index {e.args}")
            return "Ups algo salió mal con el GET"

    def POST(self):
        try:
            # Obtienes los datos del formulario
            form = web.input()
            num1 = form.num1
            num2 = form.num2

            # Realizas el cálculo llamando al método del modelo
            resultado = m_index.calcular(num1, num2)

            # Renderizas la plantilla con el resultado y los valores de num1 y num2
            return render.index(datos=resultado, num1=num1, num2=num2)
        except Exception as e:
            print(f"Error al procesar la solicitud: {e}")
            return "Ups, algo salió mal en el POST"