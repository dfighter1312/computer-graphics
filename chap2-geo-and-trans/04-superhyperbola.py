from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math
import sympy

#Width and height of the eclipse
W = 0.8
H = 0.8
n = 0.2

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, 0.0, 1.0)

def keyPressed(*args):
    global n
    if args[0] == GLUT_KEY_UP and n < 5.0:
        n += 0.1
    if args[0] == GLUT_KEY_DOWN and n >= 0.2:
        n -= 0.1
    print(n)


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

def draw_supereclipse():
    """
    Draw the supereclipse.
    """

    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    range = np.arange(-math.pi, math.pi * (1 + 0.01) , math.pi * 0.01)
    for t in range:
        x = W * sympy.sec(t) * abs(sympy.sec(t)**(2/n - 1))
        y = H * math.tan(t) * abs(math.tan(t)**(2/n - 1))
        glVertex2f(x, y)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    draw_coor()
    draw_supereclipse()
    
    glFlush()

def main():
    global window 

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(480, 480)
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Supereclipse")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutSpecialFunc(keyPressed)
    InitGL()
    glutMainLoop()

if __name__ == "__main__":
    main()