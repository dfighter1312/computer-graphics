from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math

angle = 0

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -10.0, 10.0)

def keyPressed(*args):
    global angle
    if args[0] == GLUT_KEY_LEFT:
        angle -= 5
    if args[0] == GLUT_KEY_RIGHT:
        angle += 5

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
    global end

    b = 0.2
    R = 0.5
    pipeR = 0.15
    point = list()

    for t in np.arange(0, 50, 0.5):
        x = R * math.cos(t)
        y = R * math.sin(t)
        z = b * t
        point.append(plot_circle((x, y, z), pipeR))
    
    glColor3f(1.0, 1.0, 1.0)
    for i in range(len(point) - 1):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(len(point[i])):
            glVertex3f(*point[i+1][j])
            glVertex3f(*point[i][j])
        glVertex3f(*point[i+1][0])
        glEnd()

def plot_circle(point, radius):
    point_lst = list()
    for theta in np.arange(0, (2+1/6)*math.pi, math.pi/6):
        x = radius * math.cos(theta) + point[0]
        y = radius * math.sin(theta) + point[1]
        z = point[2]
        point_lst.append((x, y, z))
    return point_lst

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.7, 0.5, 0.3, 0, 0, 0, 0, 1, 0)
    glRotatef(angle, 0, 1, 0)
    
    draw_coor()
    draw_helix()

    glFlush()

def main():
    global window 

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(720, 720)
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Helix")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutSpecialFunc(keyPressed)
    InitGL()
    glutMainLoop()

if __name__ == "__main__":
    main()