from gopigo import *
import time

TOP_DIST = 75

class PiGo:

    #####
    ##### BASIC STATUS AND METHODS
    #####

    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175, 'rightspeed' : 175, "dist" : 100}

    ismoving = False
    servoPos = 90

    def __init__(self):
        print "Hey, What's up, Hello!?!"
        self.status["dist"] = us_dist(15)

    def stop(self):
        self.status["ismoving"] = False
        print "Whoa there!"
        for x in range(3):
            stop()

    def fwd(self):
        self.ismoving = True
        print "Let's get going!"
        for x in range(3):
            fwd()

    def keepGoing(self):
        if self.status["dist"] < STOP_DIST:
            return False
        elif volt() > 14 or volt() < 6:
            print "My voltage is out the safe operation range: " + str(volt())
        else:
            return True

    def checkDist(self):
        self.status["dist"] = us_dist(15)
        print "I see something " + str(self.status["dist"]) + "mm away."

    #####
    ##### COMPLEX METHODS
    #####

    def safeDrive(self):
        self.fwd()
        while self.keepGoing():
            self.checkDist()
        self.stop()

    def servoSweep(self):
        for ang in range(20, 160, 5):
            servo(ang)
            time.sleep(.1)

    def dance(self):
        print "I just want to DANCE!"
        self.spin()
        self.shuffle()
        self.shakeServo()
        self.rturn()
        self.lturn()
        self.blink()

    def strobe(self):
        print "let's have a rager!"
        for x in range(7):
            led_on(1)
            led_off(0)
            led_off(1)
            led_on(0)

    def keyControl(self): #https://github.com/DexterInd/GoPiGo/blob/master/Software/Python/Examples/Basic_Robot_Control/basic_robot.py#
        while True:
            print "Enter the Command:",
            a=raw_input()	# Fetch the input from the terminal
            if a == 'w':
                fwd()  # Move forward
            elif a == 'a':
                left()  # Turn left
            elif a == 'd':
                right()	# Turn Right
            elif a == 's':
                bwd()  # Move back
            elif a == 'q':
                stop()  # Stop
            elif a == 'z':
                increase_speed()  # Increase speed
            elif a == 'x':
                decrease_speed()  # Decrease speed
            elif a == 'r'
                dance()  # Dance!
            elif a == 'e':
                print "Exiting"		# Exit
                sys.exit()
            else:
                print "Wrong Command, Please Enter Again"
            time.sleep(.1)

    #####
    ##### MAIN APP STARTS HERE
    #####

piggy = PiGo()

while piggy.keepGoing():
    piggy.checkDist()
    piggy.fwd()
    piggy.sleep(2)
    piggy.stop()
