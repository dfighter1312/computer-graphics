from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import cos, sin

PI = 3.141592

def model():
    return None

def gasket(depth, p1, p2, p3):
    if depth == 0:
        glVertex2f(*p1)
        glVertex2f(*p2)
        glVertex2f(*p3)
        return
    
    m1 = (p1+p2)/2
    m2 = (p2+p3)/2
    m3 = (p3+p1)/2
    
    gasket(depth-1, p1, m1, m3)
    gasket(depth-1, m1, p2, m2)
    gasket(depth-1, m3, m2, p3)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    gasket(4, np.array([cos(0), sin(0)]), np.array([cos(2*PI/3), sin(2*PI/3)]), np.array([cos(-2*PI/3), sin(-2*PI/3)]))
    glEnd()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(640, 640)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutCreateWindow("sierpinski triangle")
    init()
    # glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0)
    glutDisplayFunc(display)
    glutMainLoop()
    

if __name__ == "__main__":
    main()
