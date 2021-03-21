from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos

PI = 3.141592
gPoints = []
def model():
    
    points = []
    
    
    thetaCount = 20
    radiusStep = 0.1
    radiusCount = 30
    
    for j in range(radiusCount):
        radius = j*radiusStep
        points.append([])
        for i in range(thetaCount):
            theta = i* 2*PI/thetaCount;
            x = radius*cos(theta)
            y = radius*sin(theta)
            z = x**2 + y**2
            
            points[-1].append((x,y,z))
    
        
    return points # tuple3[][]


def animation(v):
    # glRotatef(0.1, 0., 0., 1.)
    glRotatef(1., 1., 0., 1.)
    glutPostRedisplay()
    glutTimerFunc(1000//60, animation, 0)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def display():
    global gPoints
    
    glClear(GL_COLOR_BUFFER_BIT)
    # x,y,z axis    
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0); glVertex3f(0.0,0.0,0.0); glVertex3f(10.0,0.0,0.0) # x
    glColor3f(0.0, 1.0, 0.0); glVertex3f(0.0,0.0,0.0); glVertex3f(0.0,10.0,0.0) # y
    glColor3f(0.0, 0.0, 1.0); glVertex3f(0.0,0.0,0.0); glVertex3f(0.0,0.0,10.0) # z
    glEnd()
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    
    glColor3f(1.0, 1.0, 1.0)
    m = len(gPoints)
    n = len(gPoints[0])
    for i in range(m-1):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n):
            glVertex3f(*gPoints[i+1][j])
            glVertex3f(*gPoints[i][j])
        glVertex3f(*gPoints[i+1][0])
        
        glEnd()
            
            
    glutSwapBuffers()

def main():
    glutInit()
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(640, 640)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutCreateWindow("test")
    init()
    minMax = (-10, 10)
    glOrtho(*minMax, *minMax, *minMax)
    
    # glRotatef(120., 1., 0., 0.)
    # glRotatef(45., 1., 0., 0.)
    glutTimerFunc(1, animation, 0)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    gPoints = model()
    main()

