from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def InitGL(Width, Height):
    
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glColor3f(0.0, 0.0, 0.0)
    glLoadIdentity()
    gluOrtho2D(0, 480, 0, 640)

def DrawParabola():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glBegin(GL_POINTS)

    glColor3f(0.0, 1)

    glEnd()

def main():
    global window 

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(200,200)

    window = glutCreateWindow('OpenGL Python Parabola')

    glutDisplayFunc(DrawParabola)
    InitGL(640,480)
    glutMainLoop()

if __name__ == "__main__":
    main()