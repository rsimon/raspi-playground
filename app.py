import cherrypy
import os
import RPi.GPIO as GPIO
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import WebSocket

WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

class ControlWebSocket(WebSocket):

    p = GPIO.PWM(23, 50)
    p.start(7.5)

    def opened(self):
        cherrypy.log('Opened Connection')

    def received_message(self, message):
        cherrypy.log(str(message))
        if str(message) == 'left':
            cherrypy.log('LEFT')
            ControlWebSocket.p.ChangeDutyCycle(2.5)
        elif str(message) == 'right':
            cherrypy.log('RIGHT')
            ControlWebSocket.p.ChangeDutyCycle(12.5)

        self.send(message.data, message.is_binary)

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

#cherrypy.quickstart(App(), "/", "app.config")

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
        'tools.websocket.handler_cls': ControlWebSocket
    }

})
