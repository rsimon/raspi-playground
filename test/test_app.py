import cherrypy
import os
import threading
import time
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import WebSocket

WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

class ExampleWebSocket(WebSocket):

    def poll_thread(conn):
        count = 0
        while count < 5:
            time.sleep(2)
            count += 1
            conn.send("Yay!")

    def opened(self):
        try:
            t = threading.Thread(target = self.poll_thread)
            t.start()
        except:
            cherrypy.log('Error: unable to start thread')

    def received_message(self, message):
        cherrypy.log(str(message));
        # self.send(message.data, message.is_binary)

class App(object):

    @cherrypy.expose
    def index(self):
        return file("app.html")

    @cherrypy.expose
    def on(self):
        return

    @cherrypy.expose
    def off(self):
        return

    @cherrypy.expose
    def ws(self):
        pass

cherrypy.quickstart(App(), config = {
    'global' : {
        'server.socket_host': '0.0.0.0'
    },
    '/' : {
        'tools.sessions.on': True,
        'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__))
    },
    '/static' : {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'static'
    },
    '/ws' : {
        'tools.websocket.on': True,
        'tools.websocket.handler_cls': ExampleWebSocket
    }
})
