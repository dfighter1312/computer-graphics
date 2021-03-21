from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import serial
import os
import threading
import numpy as np

ESCAPE = '\033'
 
window = 0
 
#rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0
 
DIRECTION = 1
        
# Initialize
def initGL():
    glClearColor(0, 0.1, 0.1, 1.0)
    glColor3f(1.0, 1.0, 1.0)

    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-2, 2, -1.5, 1.5, 1, 40)

    glMatrixMode(GL_MODELVIEW)
 

def display():
    global X_AXIS,Y_AXIS,Z_AXIS
    global DIRECTION

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    glTranslatef(0.0,0.0,-6.0)

    glRotatef(X_AXIS,1.0,0.0,0.0)
    glRotatef(Y_AXIS,0.0,1.0,0.0)
    glRotatef(Z_AXIS,0.0,0.0,1.0)
    # Draw the tetrahedron
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(0, 1, 0) 
    glVertex3f(0, 4, 0)

    glColor3f(1, 1, 0) 
    glVertex3f(-2, 0, 2)

    glColor3f(0, 1, 1) 
    glVertex3f(2, 0, 2)

    glColor3f(1, 1, 1) 
    glVertex3f(0, 0, -2.8)

    glColor3f(1, 0, 0) 
    glVertex3f(0, 4, 0)

    glColor3f(0, 0, 1) 
    glVertex3f(-2, 0, 2)
    glEnd()
    X_AXIS = X_AXIS - 0.05
    Z_AXIS = Z_AXIS - 0.05
 
    glutSwapBuffers()

# main function
def main():
    global window
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(200,200)
    window = glutCreateWindow("Tetrahedron")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    # Instantiate the cube
    initGL()
    glutMainLoop()

# Call the main function
if __name__ == '__main__':
    main()
