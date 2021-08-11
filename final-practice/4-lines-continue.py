from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def initGL():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 100, 0, 100)

def plotLine(x1, y1, x2, y2):
    # 1. Calculate change in X and Y.
    deltaX = x2-x1
    deltaY = y2-y1
    # 2. Calculate Steps. 
    steps = 0
    if(abs(deltaX)>abs(deltaY)):
        steps = abs(deltaX)
    else:
        steps = abs(deltaY)
    # 3. Calculate X & Y increment.
    Xincrement = deltaX/steps
    Yincrement = deltaY/steps

    # Finally we start ploting line :)

    glClear(GL_COLOR_BUFFER_BIT) # RE1002 This is to clear everything we previously drawn, if any
    glColor3f(1.0,0.0,0.0) # RE1007 This will set color RGB(1,0,0) which is red
    glPointSize(10.0) # RE1011 this will set the point with a specific radius that we give
    glBegin(GL_POINTS) # RE1001 sets point mode

    for step in range(1,steps+1): # Loops from 1 to n for n steps
        glVertex2f(round(x1),round(y1)) # Plot the point at (x1,y1)
        x1 = x1 + Xincrement # update x1 to next X cordinate
        y1 = y1 + Yincrement # update y1 to next Y cordinate
    
    glEnd() # RE1001
    glFlush() # RE1012

def main():
    # Ask for choice
    choice = 0
    while (choice != 2):
        choice = input("Please Choose \n\t1. Plot a New line\n\t2. Exit\n")
        if int(choice) == 1:
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(0,0)
            glutCreateWindow("Plot Line using DDA | Naseem's OpenGLlabs")
            glutDisplayFunc(lambda: plotLine(x1,y1,x2,y2)) # Refer RE1013 for why the use of lambda
            glutIdleFunc(lambda: plotLine(x1,y1,x2,y2))
            initGL()
            glutMainLoop()
        else: 
            print("Invalid choice")
            choice = 0

if __name__ == "__main__":
    main()