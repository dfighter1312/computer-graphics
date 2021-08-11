from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(9.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 640.0, 0.0, 480.0)

def mydisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glVertex2i(289, 190)
    glVertex2i(320, 128)
    glVertex2i(239, 67)
    glVertex2i(194, 101)
    glVertex2i(129, 83)
    glVertex2i(75, 73)
    glVertex2i(74, 74)
    glVertex2i(20, 20)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 150)
    glutCreateWindow("The Big Dipper")
    glutDisplayFunc(mydisplay)
    InitGL()
    glutMainLoop()

if __name__ == '__main__':
    main()