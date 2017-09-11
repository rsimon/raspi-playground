import cherrypy

class App(object):
    
    @cherrypy.expose
    def index(self):
        return file("app.html")

    @cherrypy.expose
    def on(self):
        return "On"

    @cherrypy.expose
    def off(self):
        return "Off"

if __name__ == '__main__':
    cherrypy.quickstart(App(), config = "app.config")
