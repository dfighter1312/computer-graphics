import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
 
window = 0
 
#rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0
 
DIRECTION = 1
DEGREE_TO_RADIAN = math.pi / 180.0

def InitGL(Width, Height): 
 
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0) 
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)  
    glMatrixMode(GL_PROJECTION)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def tetrahedron():
    global X_AXIS,Y_AXIS,Z_AXIS
    global DIRECTION
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
    glLoadIdentity()
    glTranslatef(0.0,0.0,-6.0)
 
    glRotatef(X_AXIS,1.0,0.0,0.0)
    glRotatef(Y_AXIS,0.0,1.0,0.0)
    glRotatef(Z_AXIS,0.0,0.0,1.0)

    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(0, 1, 0) 
    glVertex3f(0, 0.8, 0)

    glColor3f(1, 1, 0) 
    glVertex3f(-0.4, 0, 0.4)

    glColor3f(0, 1, 1) 
    glVertex3f(0.4, 0, 0.4)

    glColor3f(1, 1, 1) 
    glVertex3f(0, 0, -0.56)

    glColor3f(1, 0, 0) 
    glVertex3f(0, 0.8, 0)

    glColor3f(0, 0, 1) 
    glVertex3f(-0.4, 0, 0.4)
    glEnd()
    
    X_AXIS = X_AXIS - 0.05
    Z_AXIS = Z_AXIS - 0.05
 
    glutSwapBuffers()

def main():
    global window 
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) #Set the display mode to be colored
    glutInitWindowSize(640, 480) #Set the width and height of your window
    glutInitWindowPosition(0, 0) #Set the position at which this window should appear
    window = glutCreateWindow("OpenGL Sphere") #Set the window title
    glutDisplayFunc(tetrahedron) #Tell OpenGL to call the showScreen method continuously
    glutIdleFunc(tetrahedron)  #Keeps the window open
    InitGL(640, 480)
    glutMainLoop()      #Keeps the above created window displaying/running in a loop

if __name__ == "__main__":
    main()