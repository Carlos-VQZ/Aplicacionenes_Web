import web
from mvc.models.modelo_calculadora import ModeloCalculadora

render = web.template.render('mvc/views/', base='layout')
m_calculadora = ModeloCalculadora()

class Calculadora:
    def GET(self):
        try:
            return render.index(datos=None, num1=None, num2=None)
        except Exception as e:
            print(f"Error 101 - index {e.args}")
            return "GET ERROR"

    def POST(self):
        try:
            form = web.input()
            num1 = form.num1
            num2 = form.num2

            resultado = m_calculadora.calcular(num1, num2)

            return render.index(datos=resultado, num1=num1, num2=num2)
        except Exception as e:
            print(f"Error al procesar la solicitud: {e}")
            return "POST ERROR"