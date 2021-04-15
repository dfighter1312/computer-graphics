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
    glOrtho(*findMinMax(), -10.0, 10.0)

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
    glVertex2f(-3.0, 0.0)
    glVertex2f(3.0, 0.0)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, -3.0)
    glVertex2f(0.0, 3.0)

    glEnd()

def findMinMax():
    min_x = math.cos(0) - math.cos(80*0) * math.sin(0)
    max_x = min_x
    for t in np.arange(0, 2*math.pi, 0.001):
        x = math.cos(t) - math.cos(80*t)*math.sin(t)
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x

    min_y = 2*math.sin(0) - math.sin(80*0)
    max_y = min_y
    for t in np.arange(0, 2*math.pi, 0.001):
        y = 2*math.sin(t) - math.sin(80*t)
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    return min_x, max_x, min_y, max_y

def draw_shape():
    """
    Draw the shape.
    """
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    for t in np.arange(0, 2*math.pi + 0.001, 0.001):
        x = math.cos(t) - math.cos(80*t)*math.sin(t)
        y = 2*math.sin(t) - math.sin(80*t)
        glVertex2f(x, y)

    glEnd()

def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_coor()
    draw_shape()

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