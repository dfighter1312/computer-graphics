from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

mode = 0
A = np.array([-0.2, -0.6])
B = np.array([0.4, 0.3])

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, 0.0, 1.0)

def keyPressed(*args):
    global mode
    if args[0] == GLUT_KEY_LEFT:
        mode = 0
    if args[0] == GLUT_KEY_DOWN:
        mode = 1
    if args[0] == GLUT_KEY_RIGHT:
        mode = 2
    display()


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
    # Mode for displaying the line segment, line and ray
    global mode

    # Coordinate of A and B
    global A, B

    range = 0
    if mode == 0:   #line segment
        range = np.arange(0, 1, 0.01)
    elif mode == 1: #line
        range = np.arange(-5, 5, 0.01)
    elif mode == 2: #ray
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
    glutSpecialFunc(keyPressed)
    InitGL()
    glutMainLoop()

if __name__ == "__main__":
    main()