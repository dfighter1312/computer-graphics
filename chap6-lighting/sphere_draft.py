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
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    
    diffuse0 = [0.5, 0.5, 0.5, 1.0]
    ambient0 = [1.0, 0.0, 0.0, 1.0]
    specular0 = [1.0, 0.0, 0.0, 1.0]
    light0_pos = [0.0, 1.0, -1.0, 1.0]

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light0_pos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse0)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    # glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

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

def special(*key):
    global X_AXIS,Y_AXIS,Z_AXIS
    # Scale the sphere up or down
    if key[0] == GLUT_KEY_UP:
        Y_AXIS += 5
    if key[0] == GLUT_KEY_DOWN:
        Y_AXIS -= 5

    if key[0] == GLUT_KEY_LEFT:
        X_AXIS += 5
    if key[0] == GLUT_KEY_RIGHT:
        X_AXIS -= 5

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

    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(0.5, 0.5, 0.5)
    for vertex in data:
        glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()
    
    # Y_AXIS = Y_AXIS - 0.5

    glutSwapBuffers()

def main():
    global window 
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) #Set the display mode to be colored
    glutInitWindowSize(640, 480) #Set the width and height of your window
    glutInitWindowPosition(0, 0) #Set the position at which this window should appear
    window = glutCreateWindow("OpenGL Sphere") #Set the window title
    glutDisplayFunc(sphere) #Tell OpenGL to call the sphere method continuously
    glutIdleFunc(sphere)  #Keeps the window open
    glutSpecialFunc(special) #Special function for key events
    InitGL(640, 480)
    glutMainLoop()      #Keeps the above created window displaying/running in a loop

if __name__ == "__main__":
    main()