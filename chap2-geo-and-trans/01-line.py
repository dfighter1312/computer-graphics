from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math
time = 0

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, 0.0, 1.0)

def draw_coor():
    """
    Draw the 2D (Oxy) coordinate.
    """
    glBegin(GL_LINE_STRIP)

    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)

    glEnd()

def draw_line():
    """
    Draw the line with respect to the 2D-coordinate
    """
    # Time for displaying the line segment, line and ray
    global time
    time += 1

    # Coordinate of A and B
    A = np.array([0.2, 0.5])
    B = np.array([-0.4, -0.3])

    range = 0
    if math.floor(time / 200.0) % 3 == 0:
        range = np.arange(0, 1, 0.01)
    elif math.floor(time / 200.0) % 3 == 1:
        range = np.arange(-5, 5, 0.01)
    elif math.floor(time / 200.0) % 3 == 2:
        range = np.arange(0, 5, 0.01) 

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    for t in range:
        v = A + (B - A) * t
        glVertex2f(*v)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    draw_coor()
    draw_line()
    
    glFlush()

def main():
    global window 

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(480, 480)
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Line")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    InitGL()
    glutMainLoop()

if __name__ == "__main__":
    main()