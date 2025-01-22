# ---------------------------------------------------------------------------- #
#                                                                              #
#   Module:       main.py                                                      #
#   Author:       vexbedford                                                   #
#   Created:      1/16/2025, 8:36:07 PM                                        #
#   Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()

## Robot Configuration

controller_1 = Controller(PRIMARY) ##This is the controller object so we can get input from the controls
conveyer = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)  #conveyor belt connect to port 1
right_motor1 = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
left_motor1 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)   #port 10 connect to the left, port 9 connect to the right
right_motor2 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
left_motor2 =Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
#swipe on 11, front black thingy on 13

FrontSpindle = Motor(Ports.PORT13, GearSetting.RATIO_18_1, False)
claw = Pneumatics(brain.three_wire_port.a)
claw.close()

 
def spindlestart():
    FrontSpindle.spin(FORWARD)
def spindlestop():
    FrontSpindle.stop()

def ClawUp():
    claw.close()
def ClawDown():
    claw.open()
   



def foward(length):
    length = length / 13.5
    right_motor1.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor1.spin_for(FORWARD,length,TURNS,wait=False)
    right_motor2.spin_for(FORWARD,length,TURNS,wait=False)  #one full turn will move 13.5 inches
    left_motor2.spin_for(FORWARD,length,TURNS,wait=True)
def backward(length):
    length = length / 13.5
    right_motor1.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor1.spin_for(REVERSE,length,TURNS,wait=False)
    right_motor2.spin_for(REVERSE,length,TURNS,wait=False)
    left_motor2.spin_for(REVERSE,length,TURNS,wait=True)
def right(degree):
    degree = degree / 90 * 0.96
    left_motor1.spin_for(FORWARD,degree,TURNS,wait=False)
    right_motor1.spin_for(REVERSE,degree,TURNS,wait=False) #0.96 spin will turn 90 degrees
    left_motor2.spin_for(FORWARD,degree,TURNS,wait=False)
    right_motor2.spin_for(REVERSE,degree,TURNS,wait=True)
def left(degree):
    degree = degree / 90 * 0.96
    right_motor1.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor1.spin_for(REVERSE,degree,TURNS,wait=False)
    right_motor2.spin_for(FORWARD,degree,TURNS,wait=False)
    left_motor2.spin_for(REVERSE,degree,TURNS,wait=True)


FrontSpindle.set_velocity(50,PERCENT)
conveyer.set_velocity(50,PERCENT) #works at 50%
controller_1.buttonR1.pressed(spindlestart)
controller_1.buttonR2.pressed(spindlestop)
controller_1.buttonL1.pressed(ClawDown)
controller_1.buttonL2.pressed(ClawUp)

def autonomous():
   
    spindlestart()
    # right_motor1.spin_for(REVERSE,34.62/13.5,TURNS,wait=False)  #one full turn will move 13.5 inches
    # left_motor1.spin_for(REVERSE,34.62/13.5,TURNS,wait=False)
    # right_motor2.spin_for(REVERSE,34.62/13.5,TURNS,wait=False)  #one full turn will move 13.5 inches
    # left_motor2.spin_for(REVERSE,34.62/13.5,TURNS,wait=True)
    backward(34.62)
    claw.open()
    conveyer.spin(FORWARD)
    right(100)
    foward(23)
    # left_motor1.spin_for(FORWARD,15/90*0.96,TURNS,wait=False)
    # right_motor1.spin_for(REVERSE,15/90*0.96,TURNS,wait=True) #0.96 spin will turn 90 degrees
    # left_motor2.spin_for(FORWARD,15/90*0.96,TURNS,wait=False)
    # right_motor2.spin_for(REVERSE,15/90*0.96,TURNS,wait=True) #0.96 spin will turn 90 degrees

   
def user_control():
    controller_1.buttonR1.pressed(spindlestart)
    controller_1.buttonR2.pressed(spindlestop)
    controller_1.buttonL1.pressed(ClawUp)
    controller_1.buttonL2.pressed(ClawDown)
    while True:

    ##MOTOR CONTROL
        right_motor1.set_velocity((controller_1.axis3.position() - controller_1.axis4.position()), PERCENT)
        left_motor1.set_velocity((controller_1.axis3.position() + controller_1.axis4.position()), PERCENT)
        right_motor2.set_velocity((controller_1.axis3.position() - controller_1.axis4.position()), PERCENT)
        left_motor2.set_velocity((controller_1.axis3.position() + controller_1.axis4.position()), PERCENT)
        conveyer.set_velocity((controller_1.axis2.position())*0.65,PERCENT)
        right_motor1.spin(FORWARD)
        left_motor1.spin(FORWARD)
        right_motor2.spin(FORWARD)
        left_motor2.spin(FORWARD)
        conveyer.spin(FORWARD)
       
        wait(5, MSEC)
   

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()

