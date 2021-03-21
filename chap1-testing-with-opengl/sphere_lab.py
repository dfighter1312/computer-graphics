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

def find_sphere_vertex():             
    vertex_data = []
    for phi in range(-90, 90 + 10, 10):
        phir = phi*DEGREE_TO_RADIAN
        phir20 = (phi + 10.0)*DEGREE_TO_RADIAN
        for theta in range(-180, 180 + 10, 10):
            thetar = theta*DEGREE_TO_RADIAN
            vertex_data.append((math.sin(thetar)*math.cos(phir),
                             math.cos(thetar)*math.cos(phir),
                             math.sin(phir)))
            vertex_data.append((math.sin(thetar)*math.cos(phir20),
                             math.cos(thetar)*math.cos(phir20),
                             math.sin(phir20)))
    return vertex_data


def sphere():
    global X_AXIS,Y_AXIS,Z_AXIS
    global DIRECTION
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
    glLoadIdentity()
    glTranslatef(0.0,0.0,-6.0)
 
    glRotatef(X_AXIS,1.0,0.0,0.0)
    glRotatef(Y_AXIS,0.0,1.0,0.0)
    glRotatef(Z_AXIS,0.0,0.0,1.0)

    data = find_sphere_vertex()

    r = 1.0
    g = 0.0
    b = 0.0
    glBegin(GL_TRIANGLE_STRIP)
    for vertex in data:
        r -= 0.001
        g += 0.002
        b += 0.001
        glColor3f(r, g, b)
        glVertex3f(vertex[0], vertex[1], vertex[2])
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
    glutDisplayFunc(sphere) #Tell OpenGL to call the showScreen method continuously
    glutIdleFunc(sphere)  #Keeps the window open
    InitGL(640, 480)
    glutMainLoop()      #Keeps the above created window displaying/running in a loop

if __name__ == "__main__":
    main()