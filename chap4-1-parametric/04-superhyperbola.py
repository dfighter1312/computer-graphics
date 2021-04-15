from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math
import sympy

#Width and height of the superhyperbola
W = 1
H = 1
n = 1

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-5.0, 5.0, -5.0, 5.0, 0.0, 1.0)

def keyPressed(*args):
    global n
    if args[0] == GLUT_KEY_UP and n < 5.0:
        n += 0.1
    if args[0] == GLUT_KEY_DOWN and n >= 0.2:
        n -= 0.1
    n = round(n, 1)
    print(n)


def draw_coor():
    """
    Draw the 2D (Oxy) coordinate.
    """
    glBegin(GL_LINE_STRIP)

    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)

    glEnd()

    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, -5.0)
    glVertex2f(0.0, 5.0)

    glEnd()

def draw_supereclipse():
    """
    Draw the supereclipse.
    """
    range1 = np.arange(-math.pi/2 + 0.01, math.pi/2, 0.05)
    range2 = np.arange(math.pi/2 + 0.01, 3*math.pi/2, 0.05)
    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_LINE_STRIP)
    for t in range1:
        x = W * sympy.sec(t) * abs(sympy.sec(t)**(2/n - 1))
        y = H * math.tan(t) * abs(math.tan(t)**(2/n - 1))
        glVertex2f(x, y)
    glEnd()

    glBegin(GL_LINE_STRIP)
    for t in range2:
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
    glutInitWindowSize(720, 720)
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Superhyperbola")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutSpecialFunc(keyPressed)
    InitGL()
    glutMainLoop()

if __name__ == "__main__":
    main()