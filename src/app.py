import cherrypy
import os
import RPi.GPIO as GPIO

from rc_handler import RemoteControlHandler

from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool

WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

class App(object):

    '''
    Remote control Web page
    '''
    @cherrypy.expose
    def index(self):
        return file("app.html")

    '''
    Switch light on
    '''
    @cherrypy.expose
    def on(self):
        GPIO.output(18, GPIO.HIGH)
        return

    '''
    Switch light off
    '''
    @cherrypy.expose
    def off(self):
        GPIO.output(18, GPIO.LOW)
        return

    '''
    Web socket connection endpoint
    '''
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
        'tools.websocket.handler_cls': RemoteControlHandler
    }
})
