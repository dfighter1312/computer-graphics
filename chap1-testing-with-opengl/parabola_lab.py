import math
import random
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

def draw_parabola():
    latCount = 20
    longCount = 20
    latDelta = math.pi/ latCount
    longDelta = 2* math.pi/longCount
    verticies = []

    for i in range(1, latCount+1):
        lat = i*latDelta
        for j in range(1, longCount+1):
            lon = j*longDelta
            rho = math.cos(lat) / (math.sin(lat)*math.sin(lat))
            x = rho*math.sin(lat)*math.cos(lon)
            y = rho*math.sin(lat)*math.sin(lon)
            z = rho * math.cos(lat)
            verticies.append((x,y,z))
    for i in range(1, latCount - 1):
        glBegin(GL_QUAD_STRIP)
        for j in range(1, longCount):
            glVertex3fv(verticies[j+i*longCount])
            # print(j, i, len(verticies))
            glVertex3fv(verticies[j+(i+1)*longCount])
        glEnd()


def parabola():
    global X_AXIS,Y_AXIS,Z_AXIS
    global DIRECTION
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
    glLoadIdentity()
    glTranslatef(-6.0,-6.0,-20.0)
 
    glRotatef(X_AXIS,1.0,0.0,0.0)
    glRotatef(Y_AXIS,0.0,1.0,0.0)
    glRotatef(Z_AXIS,0.0,0.0,1.0)

    draw_parabola()
    
    X_AXIS = X_AXIS - 0.30
    Z_AXIS = Z_AXIS - 0.30
 
    glutSwapBuffers()

def main():
    global window 
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) #Set the display mode to be colored
    glutInitWindowSize(640, 480) #Set the width and height of your window
    glutInitWindowPosition(0, 0) #Set the position at which this window should appear
    window = glutCreateWindow("OpenGL Sphere") #Set the window title
    glutDisplayFunc(parabola) #Tell OpenGL to call the showScreen method continuously
    glutIdleFunc(parabola)  #Keeps the window open
    InitGL(640, 480)
    glutMainLoop()      #Keeps the above created window displaying/running in a loop

if __name__ == "__main__":
    main()