from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def printMatrix(matrix):
    for i in range(4):
        print("{:.4f} {:.4f} {:.4f} {:.4f}".format(matrix[i], matrix[i + 4], matrix[i + 8], matrix[i + 12]))

def printModelViewMatrix():
    matrix = np.zeros(16)
    result = glGetFloatv(GL_MODELVIEW_MATRIX, matrix)
    printMatrix(result)

def InitGL():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0, 0, 0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(-10.0, 10.0, -10.0, 10.0, 0.0, 1.0)

    glMatrixMode(GL_MODELVIEW) # opengl uses model view matrix
    glLoadIdentity() # initialized with identity matrix
    

def drawGrid():
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(0.0, 5.0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    print("In line 9")
    printModelViewMatrix()
    drawGrid()

    gluPerspective(45.0, 1.0, 0.1, 100.0)
    print("In line 11")
    printModelViewMatrix()
    glRotatef(45.0, 0.0, 0.0, 1.0)
    print("In line 12")
    printModelViewMatrix()
    glScalef(0.5, 0.5, 1.0)
    print("In line 13")
    printModelViewMatrix()
    drawGrid()
    
    glFlush()

def main():
    global window
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(480, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Simple")
    glutDisplayFunc(display)
    InitGL()
    glutMainLoop()

if __name__ == "__main__":
        main() 