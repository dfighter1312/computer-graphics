from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math

angle = 0

X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -10.0, 10.0)

# def keyPressed(*args):
#     global angle
#     if args[0] == GLUT_KEY_LEFT:
#         angle -= 5
#     if args[0] == GLUT_KEY_RIGHT:
#         angle += 5

def draw_coor():
    """
    Draw the 3D (Oxy) coordinate.
    """
    glBegin(GL_LINE_STRIP)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -1.0)
    glVertex3f(0.0, 0.0, 1.0)

    glEnd()

def draw_helix():
    """
    Draw the helix.
    """
    a = 0.5
    b = 1
    c = 10

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    for t in np.arange(0, 40, 0.01):
        x = (a*math.sin(c*t) + b) * math.cos(t)
        y = (a*math.sin(c*t) + b) * math.sin(t)
        z = a * math.cos(c*t)
        glVertex3f(x, y, z)

    glEnd()

def display():
    global X_AXIS, Y_AXIS, Z_AXIS

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.5, 0.5, 0.3, 0, 0, 0, 0, 1, 0)
    glRotatef(X_AXIS,1.0,0.0,0.0)
    glRotatef(Y_AXIS,0.0,1.0,0.0)
    glRotatef(Z_AXIS,0.0,0.0,1.0)
    draw_coor()
    draw_helix()
    
    X_AXIS -= 0.3
    Y_AXIS -= 0.3
    Z_AXIS -= 0.3

    glFlush()

def main():
    global window 

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(720, 720)
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Line")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    # glutSpecialFunc(keyPressed)
    InitGL()
    glutMainLoop()

if __name__ == "__main__":
    main()