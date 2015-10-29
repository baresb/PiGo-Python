from gopigo import *
import time

class PiGo:

    isMoving = False
    servoPos = 90

    def __init__(self):
        print "Hey, What's up, Hello!?!"

    def stop(self):
        self.isMoving = False
        while stop() != 1:
            time.sleep(.1)
            print "I'm sorry I was born a little glitchy"

    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.sleep(.1)
            print "My moving parts are very sore"

piggy = PiGo()
tina.fwd()
time.sleep(2)
tina.stop()
