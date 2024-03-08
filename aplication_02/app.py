import web
from mvc.controllers.index import CalculadoraControlador

# Definir las URLs y el objeto de renderizado
urls = (
    "/", "mvc.controllers.index.CalculadoraControlador",
)

render = web.template.render('mvc/views/')

# Crear la aplicación web
app = web.application(urls, globals())

if __name__ == "__main__":
    # Configurar la aplicación para no estar en modo de depuración
    web.config.debug = True

    # Ejecutar la aplicación web
    app.run()
