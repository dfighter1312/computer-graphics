from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import sin, cos

PI = 3.141592

def cylinderModel():
    points = []
    radius = 0.5
    for z in np.arange(-0.8, 1., 0.1):
        points.append([])
        for theta in np.arange(0., 2*PI, PI/20):
            x = radius*cos(theta)
            y = radius*sin(theta)
            points[-1].append((x,y,z))
            
    return points
            
def torusModel():
    points = []
    majorRadius = 0.5
    minorRadius = 0.1
    for theta in np.arange(0, 2*PI, PI/12):
        points.append([])
        for phi in np.arange(-PI/2, PI/2+PI/12, PI/12):
            y = (majorRadius + minorRadius*cos(theta))*cos(phi) + 0.5
            z = (majorRadius + minorRadius*cos(theta))*sin(phi)
            x = minorRadius*sin(theta)
            points[-1].append((x,y,z))
    return points

def cupBaseModel():
    points = [(0,0,-0.8)]
    radius = 0.5
    for theta in np.arange(0., 2*PI, PI/12):
        x = radius*cos(theta)
        y = radius*sin(theta)
        z = -0.8
        points.append((x,y,z))
        
    return points
            

def model():
    # a cylinder and a half of torus
    cylinder = cylinderModel()
    torus = torusModel()    
    # assembly this to form a cup
    # for strip in torus:
    #     for i in range(len(strip)):
    #         point = strip[i]
    #         point = (point[0], point[1] + 0.5, point[2])
    #         strip[i] = point
    #         # vec = np.array(point)
    #         # # print(vec)
    #         # point = tuple(vec + np.array([0., 5., 0.]))
    return (cylinder, torus, cupBaseModel())
gModel = model()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def animation(v):
    glRotatef(1., 1., 0., 1.)
    glutPostRedisplay()
    glutTimerFunc(16, animation, 0)

def display():
    
    def drawModel(model, loop=True):
        m = len(model)
        n = len(model[0])
        for i in range(m-1):
            glBegin(GL_TRIANGLE_STRIP)
            for j in range(n):
                glVertex3f(*model[i+1][j])
                glVertex3f(*model[i][j])
            if loop:
                glVertex3f(*model[i+1][0])
            
            glEnd()    
            
    global gModel
    cylinder, torus, cupBase = gModel
    glClear(GL_COLOR_BUFFER_BIT)
    
    # x,y,z axis    
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0); glVertex3f(0.0,0.0,0.0); glVertex3f(10.0,0.0,0.0) # x
    glColor3f(0.0, 1.0, 0.0); glVertex3f(0.0,0.0,0.0); glVertex3f(0.0,10.0,0.0) # y
    glColor3f(0.0, 0.0, 1.0); glVertex3f(0.0,0.0,0.0); glVertex3f(0.0,0.0,10.0) # z
    glEnd()
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glColor3f(1.0, 1.0, 1.0)
    drawModel(cylinder)
    drawModel(torus, False)
    
    glBegin(GL_TRIANGLE_FAN)
    for point in cupBase:
        glVertex3f(*point)
    glEnd()
    
    glutSwapBuffers()

def main():
    glutInit()
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(640, 640)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutCreateWindow("test")
    init()
    glRotatef(-90., 1., 0., 0.)
    glutTimerFunc(0, animation, 0)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()

