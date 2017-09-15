import cherrypy
import os
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import WebSocket
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(18, GPIO.OUT)
#GPIO.setup(23, GPIO.OUT)

#p = GPIO.PWM(23, 50)
#p.start(7.5)

class EchoWebSocket(WebSocket):

    def received_message(self, message):
        self.send(message.data, message.is_binary)

WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

class App(object):

    @cherrypy.expose
    def index(self):
        return file("app.html")

    @cherrypy.expose
    def on(self):
        #GPIO.output(18, GPIO.HIGH)
        return

    @cherrypy.expose
    def off(self):
        #GPIO.output(18, GPIO.LOW)
        return

    @cherrypy.expose
    def left(self):
        #p.ChangeDutyCycle(2.5)
        return

    @cherrypy.expose
    def right(self):
        #p.ChangeDutyCycle(12.5)
        return

    @cherrypy.expose
    def ws(self):
        pass

#cherrypy.quickstart(App(), "/", "app.config")

cherrypy.quickstart(App(), config = {
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
        'tools.websocket.handler_cls': EchoWebSocket
    }

})
