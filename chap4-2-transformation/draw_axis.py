from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

O = np.array([0.0, 0.0])
A = np.array([1.0, 0.7])
B = np.array([0.0, 1.0])

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
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

def draw_tile(point1, point2, tile_length, n):
    #Parametric form of OA and OB
    def line(t):
        return point1 + (point2 - point1) * t
    def length(vector):
        return (vector[0] ** 2 + vector[1] ** 2) ** (1/2)
    def norm(vector):
        return np.array([-vector[1], vector[0]]) / length(vector)
    
    for t in range(1, n):
        glBegin(GL_LINE_STRIP)
        p1 = line(t / n) + norm(point2 - point1) * tile_length
        p2 = line(t / n) - norm(point2 - point1) * tile_length
        print(p1, p2)
        glVertex2f(*p1)
        glVertex2f(*p2)
        glEnd()
    
    glBegin(GL_LINE_STRIP)
    p1F = line(0.95) + norm(point2 - point1) * tile_length
    p2F = line(0.95) - norm(point2 - point1) * tile_length
    print(p1F, p2F)
    glVertex2f(*p1F)
    glVertex2f(*point2)
    glVertex2f(*p2F)
    glEnd()
    

def draw_line():
    """
    Draw the line with respect to the 2D-coordinate
    """
    global O, A, B
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(*O)
    glVertex2f(*A)
    glVertex2f(*O)
    glVertex2f(*B)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    draw_line()
    draw_tile(O, A, 0.02, 10)
    draw_tile(O, B, 0.02, 10)

    glFlush()

def main():
    global window 

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(480, 480)
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Line")

    glutDisplayFunc(display)
    InitGL()
    glutMainLoop()

if __name__ == "__main__":
    main()