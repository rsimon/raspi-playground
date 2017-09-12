import cherrypy
import RPi.GPIO as GPIO

class App(object):

    def __init__():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)

        self.p = GPIO.PWM(23, 50)
        self.p.start(7.5)

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
    def left(self):
        print("LEFT")
        self.p.ChangeDutyCycle(2.5)
        return

    @cherrypy.expose
    def right(self):
        print "RIGHT"
        self.p.ChangeDutyCycle(12.5)
        return

cherrypy.tree.mount(App(), "/", "app.config")
