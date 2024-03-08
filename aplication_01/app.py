import web

urls = (
    "/", "Hello",
    "/pagina2", "Pagina2"
)

app = web.application(urls, globals())

class Hello:
    def GET(self):
        return "Hola página 1"

class Pagina2:
    def GET(self):
        return "Hola página 2"

if __name__ == "__main__":
    app.run()
