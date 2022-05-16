# Part 2: Gameplay
from graphics import *
import random, time

from threading import *
import threading

win = GraphWin('Red Light, Green Light', 1900, 1000)
#win.yUp() #Uncomment this portion if you are using the 2011 version of Zelle's graphics 
win.setCoords(0, 0, 1900, 1000) #Be sure to have this portion enabled if using 2016 version.
background_color = color_rgb(105, 179, 240)
win.setBackground(background_color)

'''The lines of code below will create the countdown system. The player loses if they do not make it to the end of the map.
COUNTDOWN WORKS, BUT IT HAS NOT BEEN SUCCESSFULLY THREADED INTO THE GAME. PLAYER MOVEMENTS AFFECT ITS IMPLEMENTATION. '''

def countdown():

    global count #Threading feature for countdown function. Not working as intended.
    count = 10
    seconds = time.time()

    while seconds > 0:

        t = Text(Point(1800,900), count)
        t.setSize(36)
        t.setStyle("bold")
        t.setTextColor("black")
        t.draw(win)
        time.sleep(1)
        count-=1
        t.undraw()

        if count == 0:
            message = Text(Point(win.getWidth()/2, 640), 'You died!')
            message.setSize(36)
            message.setStyle("bold")
            message.setTextColor("red")
            message.draw(win)
            break

''' The lines of code below will create the graphical environment of the gameplay section '''

def environment():
    
    p1 = Point(0, 100) #Creates the ground that the player will run on
    p1.draw(win)
    p2 = Point(1900, 0)
    p2.draw(win)
    ground = Rectangle(p1, p2)
    ground.setWidth(2)
    ground_color = color_rgb(52, 140, 49)
    ground.setFill(ground_color)
    ground.draw(win)

    p1 = Point(1680, 100) #Shows where the finish line is in a distinctive color
    p2 = Point(1900, 100)
    finishLine = Line(p1, p2)
    finishLine.setFill('orange')
    finishLine.setWidth(7)
    finishLine.draw(win)

#    countdownImage = Text(Point(200, 900, 'countdown.gif')
#    countdownImage.draw(win)

def light():

    center = Point(950,800) #Code for green light
    radius = 100
    greenLight = Circle(center, radius)
    greenLight_color = color_rgb(57, 255, 20)
    greenLight.setFill(greenLight_color)
    greenLight.setOutline('black')
    greenLight.setWidth(7)
    greenLight.draw(win)

    center = Point(950, 800) #Code for red light
    radius = 100
    redLight = Circle(center, radius)
    redLight.setFill('red')
    redLight.setOutline('black')
    redLight.setWidth(7)
    redLight.draw(win)

    return greenLight, redLight

def playerModel():

    center = Point(50, 200) #Creates the player's head
    radius = 20
    playerHead = Circle(center, radius)
    playerHead_color = color_rgb(197, 140, 133)
    playerHead.setFill(playerHead_color)
    playerHead.setOutline('black')
    playerHead.setWidth(2)
    playerHead.draw(win)

    p1 = Point(50, 180) #Creates the player's body
    p2 = Point(50, 130)
    playerBody = Line(p1, p2)
    playerBody.setWidth(4)
    playerBody.draw(win)

    p1 = Point(50, 130) #Creates the left leg of the player
    p2 = Point(35, 100)
    playerLeg1 = Line(p1, p2)
    playerLeg1.setWidth(4)
    playerLeg1.draw(win)

    p1 = Point(50, 130) #Creates the right leg of the player 
    p2 = Point(65, 100)
    playerLeg2 = Line(p1, p2)
    playerLeg2.setWidth(4)
    playerLeg2.draw(win)

    p1 = Point(50,160) #Creates the left arm of the player
    p2 = Point(30,125)
    playerArm1 = Line(p1, p2)
    playerArm1.setWidth(4)
    playerArm1.draw(win)

    p1 = Point(50,160) #Creates the right arm of the player
    p2 = Point(70,125)
    playerArm2 = Line(p1, p2)
    playerArm2.setWidth(4)
    playerArm2.draw(win)

    ''' Below are a set of key bindings for the player. '''
    
    dx, dy = 5, 0

    while True:
        keyBinding = win.checkKey() #Make sure to have graphics.py updated to latest package (2016 version, not 2011 version)!

        if keyBinding == 'd':
            playerHead.move(dx, dy)
            time.sleep(.01)
            playerBody.move(dx, dy)
            time.sleep(.01)
            playerArm1.move(dx, dy)
            time.sleep(.01)
            playerArm2.move(dx, dy)
            time.sleep(.01)
            playerLeg1.move(dx, dy)
            time.sleep(.01)
            playerLeg2.move(dx, dy)
            time.sleep(.01)
        elif keyBinding == 'a':
            playerHead.move(-dx, dy)
            playerBody.move(-dx, dy)
            playerArm1.move(-dx, dy)
            playerArm2.move(-dx, dy)
            playerLeg1.move(-dx, dy)
            playerLeg2.move(-dx, dy)
        elif keyBinding == 'Right':
            playerHead.move(dx, dy)
            playerBody.move(dx, dy)
            playerArm1.move(dx, dy)
            playerArm2.move(dx, dy)
            playerLeg1.move(dx, dy)
            playerLeg2.move(dx, dy)
        elif keyBinding == 'Left':
            playerHead.move(-dx, dy)
            playerBody.move(-dx, dy)
            playerArm1.move(-dx, dy)
            playerArm2.move(-dx, dy)
            playerLeg1.move(-dx, dy)
            playerLeg2.move(-dx, dy)

    return playerHead, playerBody, playerLeg1, playerLeg2, playerArm1, playerArm2, keyBinding

#playerModel = [playerHead, playerBody, playerLeg1, playerLeg2, playerArm1, playerArm2] #Tried creating key bindings using a list. Did not work as intended.

def dollModel():

    center = Point(1800, 300) #Creates the head of the doll
    radius = 45
    dollHead = Circle(center, radius)
    dollHead_color = color_rgb(232, 179, 162)
    dollHead.setFill(dollHead_color)
    dollHead.setOutline('black')
    dollHead.setWidth(2)
    dollHead.draw(win)

    p1 = Point(1800, 255) #Creates the body of the doll
    p2 = Point(1800, 170)
    dollBody = Line(p1, p2)
    dollBody.setWidth(5)
    dollBody.draw(win)

    p1 = Point(1800, 170) #Creates the left leg of the doll
    p2 = Point(1775, 100)
    dollLeg1 = Line(p1, p2)
    dollLeg1.setWidth(5)
    dollLeg1.draw(win)

    p1 = Point(1800, 170) #Creates the right leg of the doll
    p2 = Point(1825, 100)
    dollLeg2 = Line(p1, p2)
    dollLeg2.setWidth(5)
    dollLeg2.draw(win)

    p1 = Point(1730, 210) #Creates the entire arm of the doll (in a T-pose)
    p2 = Point(1870, 210)
    dollArm = Line(p1, p2)
    dollArm.setWidth(5)
    dollArm.draw(win)

    return dollHead, dollBody, dollLeg1, dollLeg2, dollArm

def main():
    
    countdown_thread = threading.Thread(target = countdown) #Having trouble implementing this
    countdown_thread.start() #Does not seem to work
    environment()
    light()
    dollModel()
    playerModel()

# message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.') #Scaffolding for the construction of the program
# message.draw(win) #Ignore 
    win.close()

main()

''' To-Do List for Part 2

- Create transition when player wins or loses
- Create automated timing system (Both countdown and timing of doll) '''
