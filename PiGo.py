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
        self.status["ismoving"] = False
        print "Whoa there!"
        for x in range(3):
            stop()

    def fwd(self):
        self.ismoving = True
        print "Let's get going!"
        for x in range(3):
            fwd()

    #####
    ##### COMPLEX METHODS
    #####

    #def keyControl(self): #https://github.com/DexterInd/GoPiGo/blob/master/Software/Python/Examples/Basic_Robot_Control/basic_robot.py#
        while True:
            print "Enter the Command:",
            a=raw_input()	# Fetch the input from the terminal
            if a=='w':
                fwd()	# Move forward
            elif a=='a':
                left()	# Turn left
            elif a=='d':
                right()	# Turn Right
            elif a=='s':
                bwd()	# Move back
            elif a=='q':
                stop()	# Stop
            elif a=='z':
                increase_speed()	# Increase speed
            elif a=='x':
                decrease_speed()	# Decrease speed
            elif a=='e':
                print "Exiting"		# Exit
                sys.exit()
            else:
                print "Wrong Command, Please Enter Again"
            time.sleep(.1)

    #####
    ##### MAIN APP STARTS HERE
    #####

piggy = PiGo()
piggy.fwd()
piggy.sleep(2)
piggy.stop()
