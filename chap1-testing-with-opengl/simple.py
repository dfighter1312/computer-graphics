from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def mydisplay():
    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_POLYGON);
    
    glVertex2f(-0.5, -0.5);
    glVertex2f(-0.5, 0.5);
    glVertex2f(0.5, 0.5);
    glVertex2f(0.5, -0.5);

    glEnd();
    glFlush();

def main():
    glutInit()
    glutCreateWindow("simple");
    glutDisplayFunc(mydisplay);
    glutMainLoop()

if __name__ == "__main__":
    main()