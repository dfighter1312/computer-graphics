from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

latitudes = 100
longtitudes = 100
last_time = 0
theta = 0
height = 0

# Direction of light
direction = [3.0, 0.0, 0.0, 1.0]
# Intensity of light
intensity = [0.9, 0.9, 0.9, 1.0]
# Intensity of ambient light
ambient_intensity = [0.1, 0.1, 0.1, 1.0]

def idle():
    global last_time
    time = glutGet(GLUT_ELAPSED_TIME)

    if last_time == 0 or time >= last_time + 40:
        last_time = time
        glutPostRedisplay()
  
def draw():
    glRotatef(5, 0, 2, 1)
    glutIdleFunc(idle)
    for i in range(0, latitudes + 1):
        lat0 = pi * (-0.5 + float(float(i - 1) / float(latitudes)))
        z0 = sin(lat0)
        zr0 = cos(lat0)

        lat1 = pi * (-0.5 + float(float(i) / float(latitudes)))
        z1 = sin(lat1)
        zr1 = cos(lat1)

        # Use Quad strips to draw the sphere
        glBegin(GL_QUAD_STRIP)

        for j in range(0, longtitudes + 1):
            lng = 2 * pi * float(float(j - 1) / float(longtitudes))
            x = cos(lng)
            y = sin(lng)
            
            if j <= 25:
                glColor3f(230/255, 126/255, 34/255)
            elif j <= 50:
                glColor3f(0,1,0)
            elif j <= 75:
                glColor3f(1,0,0)
            else:
                glColor3f(0,0,1)

            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)
    
        glEnd()



def init():
    glClearColor(0, 0.1, 0.1, 1.0)
    # self.compute_location()
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    myLightPosition = (0.0, 0.0, 1.0, 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, myLightPosition)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_intensity)
    glLightfv(GL_LIGHT0, GL_POSITION, direction)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, intensity)
    gluLookAt(1.5, 1, 0, 0, 0, 0, 0, 0, 1)

    # Setup the material
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(46/255, 204/255, 113/255)

    # Set shade model flat or smooth
    glShadeModel(GL_SMOOTH)
    draw()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(400, 100)
    glutCreateWindow('Sphere')

    # Instantiate the sphere object

    init()
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()