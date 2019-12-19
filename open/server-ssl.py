import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import sys
import time
from time import sleep
import ssl
import os
import RPi.GPIO as GPIO

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        lamp = [0, 0, 0]
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)

        if (GPIO.input(3) == True):
            lamp[0] = 1
        else:
            lamp[0] = 0
        if (GPIO.input(5) == True):
            lamp[1] = 1
        else:
            lamp[1] = 0
        if (GPIO.input(7) == True):
            lamp[2] = 1
        else:
            lamp[2] = 0
        mssg = str(lamp[0]) + str(lamp[1]) + str(lamp[2])
        print mssg
        self.write_message(mssg)


    def on_message(self, message):
	lamp = [0, 0, 0]
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)

        if (message == 'lamp1'):
            if (GPIO.input(3) == True):
                GPIO.output(3, False)
            else:
                GPIO.output(3, True)
        if (message == 'lamp2'):
            if (GPIO.input(5) == True):
                GPIO.output(5, False)
            else:
                GPIO.output(5, True)
        if (message == 'lamp3'):
            if (GPIO.input(7) == True):
                GPIO.output(7, False)
            else:
                GPIO.output(7, True)


        if (GPIO.input(3) == True):
            lamp[0] = 1
        else:
            lamp[0] = 0
        if (GPIO.input(5) == True):
            lamp[1] = 1
        else:
            lamp[1] = 0
        if (GPIO.input(7) == True):
            lamp[2] = 1
        else:
            lamp[2] = 0
        mssg = str(lamp[0]) + str(lamp[1]) + str(lamp[2])
        print mssg
        self.write_message(mssg)

    def on_close(self):
        print 'connection closed'

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/ws', WSHandler),
])


if __name__ == "__main__":
    GPIO.cleanup()
    ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_ctx.load_cert_chain(os.path.join("PATH HERE", "certificate.crt"),
                        os.path.join("PATH HERE", "private.key"))
    http_server = tornado.httpserver.HTTPServer(application, ssl_options=ssl_ctx)
    http_server.listen(5000)
    myIP = socket.gethostbyname(socket.gethostname())
    print '*** Websocket Server Started at %s***' % myIP
    tornado.ioloop.IOLoop.instance().start()
