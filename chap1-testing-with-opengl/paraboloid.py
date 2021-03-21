import pygame
import numpy as np
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def sphere(latCount, longCount):
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
            verticies.append([x,y,z])
    for i in range(1, latCount - 1):
        glBegin(GL_QUAD_STRIP)
        for j in range(1, longCount):
            glVertex3fv(verticies[j+i*longCount])
            print(j, i, len(verticies))
            glVertex3fv(verticies[j+(i+1)*longCount])
        glEnd()

def main():
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    # glScalef(0.1, 0.1, 0.1)
    glTranslatef(1, 0.0, -5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        sphere(50,50)
        glRotatef(-3, 1, 1, 0)
        pygame.display.flip()
        pygame.time.wait(10)

main()