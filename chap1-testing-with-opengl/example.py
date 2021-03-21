from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def square():
    glColor3f(1.0, 0.0, 0.0) #Set the color to red
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(0, 0)
    glVertex2f(1, 0)
    glVertex2f(0, 1)
    glVertex2f(1, 1)
    glEnd()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(0, 640, 0, 480, -10, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    square() #Draw a square using our function
    glutSwapBuffers()

def main():
    global window 
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) #Set the display mode to be colored
    glutInitWindowSize(640, 480) #Set the width and height of your window
    glutInitWindowPosition(0, 0) #Set the position at which this window should appear
    window = glutCreateWindow("OpenGL Example") #Set the window title
    glutDisplayFunc(showScreen) #Tell OpenGL to call the showScreen method continuously
    glutIdleFunc(showScreen)  #Keeps the window open
    InitGL(640, 480)
    glutMainLoop()      #Keeps the above created window displaying/running in a loop

if __name__ == "__main__":
    main()