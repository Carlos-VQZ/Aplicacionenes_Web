import web
from mvc.controllers.detalle import Detalle

# Habilitar la configuración de depuración
web.config.debug = True

# Definir las URLs y el objeto de renderizado
urls = (
    '/', 'mvc.controllers.index.Index',
    '/insertar', 'mvc.controllers.insertar.Insertar',
    '/detalle', 'mvc.controllers.detalle.Detalle',
    '/borrar', 'mvc.controllers.borrar.Borrar',
    '/actualizar', 'mvc.controllers.actualizar.Actualizar'
)

render = web.template.render('mvc/views/')

# Crear la aplicación web
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
