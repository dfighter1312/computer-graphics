from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width = 500
height = 500

GLOBAL_X = 0.0
FPS = 60.0

def square():
    """Define vertices of square to draw."""
    glBegin(GL_QUADS)
    glVertex2f(GLOBAL_X, 100)       # Bottom left
    glVertex2f(GLOBAL_X + 100, 100) # Bottom right
    glVertex2f(GLOBAL_X + 100, 200) # Top right
    glVertex2f(GLOBAL_X, 200)       # Top left
    glEnd()
    glutSwapBuffers()

def update(value):
    global GLOBAL_X
    global FPS
    glutPostRedisplay()
    glutTimerFunc(int(1000 / FPS), update, int(0))
    GLOBAL_X += 1.0

def showScreen():
    """Show stuff on screen."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from the screen
    glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 3.0) # Gives color to the following code
    square()  # Draw a square

def iterate():
    """Spot the moment when it actually draws the square."""
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 2000.0, 0.0, 2000.0, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE) # Set the display mode to be colored
    glutInitWindowSize(width, height)
    glutInitWindowPosition(50, 50)

    window = glutCreateWindow("LAB 2 | SQUARE")

    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen) # Keeps the window open
    glutTimerFunc(int(0), update, int(0))
    glutMainLoop() # Keeps the above created window displaying in a loop

if __name__ == "__main__":
    main()