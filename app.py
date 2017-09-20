import cherrypy
import os
import threading
import time
import RPi.GPIO as GPIO
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import WebSocket

WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

class ExampleWebSocket(WebSocket):

    p = GPIO.PWM(23, 50)
    p.start(7.5)

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

class App(object):

    @cherrypy.expose
    def index(self):
        return file("app.html")

    @cherrypy.expose
    def on(self):
        GPIO.output(18, GPIO.HIGH)
        return

    @cherrypy.expose
    def off(self):
        GPIO.output(18, GPIO.LOW)
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
