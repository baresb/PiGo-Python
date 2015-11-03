from gopigo import *
import time

class PiGo:

    #####
    ##### BASIC STATUS AND METHODS
    #####

    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175, 'rightspeed' : 175}

    ismoving = False
    servoPos = 90

    def __init__(self):
        print "Hey, What's up, Hello!?!"

    def stop(self):
        self.ismoving = False
        while stop() != 1:
            time.sleep(.1)
            print "I'm sorry I was born a little glitchy"

    def fwd(self):
        self.ismoving = True
        while fwd() != 1:
            time.sleep(.1)
            print "My moving parts are very sore"

    #####
    ##### COMPLEX METHODS
    #####

    #####
    ##### MAIN APP STARTS HERE
    #####

piggy = PiGo()
piggy.fwd()
piggy.sleep(2)
piggy.stop()
