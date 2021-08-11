from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math

angle = 0
end = 10
angley = 0

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # glEnable(GL_DEPTH_TEST)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    myLightPosition = (0.0, 0.0, 1.0, 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, myLightPosition)
    glShadeModel(GL_SMOOTH)

    amb0 = (1.0, 1, 1.0, 1.0)
    diff0 = (0.8, 0.9, 0.5, 1.0)
    spec0 = (0.0, 0.0, 1.0, 1.0)

    glLightfv(GL_LIGHT0, GL_AMBIENT, amb0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diff0)
    glLightfv(GL_LIGHT0, GL_SPECULAR, spec0)


    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -10.0, 10.0)

def keyPressed(*args):
    global angle, angley
    if args[0] == GLUT_KEY_UP:
        angley -= 5
    if args[0] == GLUT_KEY_DOWN:
        angley += 5
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

  
def sphere():

    glPushMatrix()
    latCount = 50
    longCount = 50
    radius = 0.5
    latDelta = math.pi/ latCount
    longDelta = 2* math.pi/longCount
    verticies = []

    for i in range(latCount+1):
        lat = i*latDelta
        for j in range(longCount+1):
            lon = j*longDelta
            x = radius*math.sin(lat)*math.cos(lon)
            y = radius*math.sin(lat)*math.sin(lon)
            z = radius * math.cos(lat)
            verticies.append([x,y,z])
    
    # glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(latCount+1):
        if i <= latCount / 4:
            glColor3f(0.5, 0.5, 0.5)
        elif i <= latCount / 2:
            glColor3f(1.0, 0.0, 0.0)
        elif i <= 3 * latCount / 4:
            glColor3f(0.0, 1.0, 0.0)
        else:
            glColor3f(0.0, 0.0, 1.0)
        for j in range(longCount+1):
            glVertex3fv(verticies[j+i*longCount])
            glVertex3fv(verticies[j+(i+1)*longCount])
    glEnd()
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.5, 0.5, 0.5, 0, 0, 0, 0, 1, 0)
    glRotatef(angle, 0, 1, 0)
    glRotatef(angley, 1, 0, 0)
    draw_coor()
    sphere()
    
    glFlush()

def main():
    global window 

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(720, 720)
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Cube")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutSpecialFunc(keyPressed)
    InitGL()
    glutMainLoop()

if __name__ == "__main__":
    main()