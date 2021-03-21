from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import serial
import os
import threading
import math
 
ESCAPE = '\033'
 
window = 0
 
#rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0
 
DIRECTION = 1
 
 
def InitGL(Width, Height): 
 
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0) 
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)   
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
 
def keyPressed(*args):
        if args[0] == ESCAPE:
                sys.exit()
 
def find():
    DEGREE_TO_RADIAN = math.pi / 180.0
    strip_data = []
    strip_data.append((0.0, 0.0, 1.0))
    sin80 = math.sin(80.0 * DEGREE_TO_RADIAN)
    cos80 = math.cos(80.0 * DEGREE_TO_RADIAN)
    for theta in range(-180, 180 + 20, 20):
        thetar = theta * DEGREE_TO_RADIAN
        strip_data.append((math.sin(thetar)*cos80, math.cos(thetar)*cos80, sin80))
    strip_data.append((0.0, 0.0, -1.0))
    for theta in range(-180, 180 + 20, 20):
        thetar = theta
        strip_data.append((math.sin(thetar)*cos80, math.cos(thetar)*cos80, sin80))
    return strip_data

def DrawGLScene():
        global X_AXIS,Y_AXIS,Z_AXIS
        global DIRECTION
 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
        glLoadIdentity()
        glTranslatef(0.0,0.0,-6.0)
 
        glRotatef(X_AXIS,1.0,0.0,0.0)
        glRotatef(Y_AXIS,0.0,1.0,0.0)
        glRotatef(Z_AXIS,0.0,0.0,1.0)
        strip_data = find()
        print(strip_data[:10])
        # Draw Cube (multiple quads)
        glBegin(GL_QUADS)
 
        

        glEnd()
 
 
        X_AXIS = X_AXIS - 0.30
        Z_AXIS = Z_AXIS - 0.30
 
        glutSwapBuffers()
 
 
 
def main():
 
        global window
 
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640,480)
        glutInitWindowPosition(200,200)

        window = glutCreateWindow('OpenGL Python Cube')
 
        glutDisplayFunc(DrawGLScene)
        glutIdleFunc(DrawGLScene)
        glutKeyboardFunc(keyPressed)
        InitGL(640, 480)
        glutMainLoop()
 
if __name__ == "__main__":
        main() 
