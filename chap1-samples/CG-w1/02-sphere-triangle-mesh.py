from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos

PI = 3.141592
gPoints = []
def model():
    
    points = []
    radius = 0.6
    stepPhi = PI/20 # longitude
    stepTheta = 2*PI/20 # latitude
    
    countPhi = 50
    countTheta = 50
    
    for i in range(countPhi+1):
        phi = -PI/2 + i*PI/countPhi
        points.append([])
        for j in range(countTheta):
            theta = j*2*PI/countTheta
            x = radius*cos(phi)*cos(theta)
            y = radius*cos(phi)*sin(theta)
            z = radius*sin(phi)
            
            points[-1].append((x,y,z))
    
    # phi = -PI/2
    # while phi < PI/2:
        
    #     theta = 0
    #     points.append([])
    #     while theta < 2*PI:
    #         x = radius*cos(phi)*cos(theta)
    #         y = radius*cos(phi)*sin(theta)
    #         z = radius*sin(phi)
            
    #         points[-1].append((x,y,z))
            
    #         # points.append((x,y,z))
            
    #         theta += stepTheta
            
    #     phi += stepPhi
        
    return points # tuple3[][]


def animation():
    # glRotatef(0.1, 0., 0., 1.)
    glRotatef(0.1, 1., 0., 1.)
    glutPostRedisplay()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def display():
    global gPoints
    
    glClear(GL_COLOR_BUFFER_BIT)
    # glBegin(GL_POINTS)
    # glColor3f(1.0, 1.0, 1.0)
    # for circle in gPoints:
    #     for x,y,z in circle:
    #         glVertex3f(x,y,z)
    # glEnd()
    
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
    glRotatef(30., 1., 0., 0.)
    # glRotatef(45., 0., 0., 1.)
    glutIdleFunc(animation)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    gPoints = model()
    main()

