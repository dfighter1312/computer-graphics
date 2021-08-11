from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initGL():
    """Initialization function."""
    glClearColor(0.5, 0.5, 0.5, 1.0) # Clea the screen and set a color
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Set up a 2D orthographic

def hLine(x_min, x_max, y):
    """
    Plot horizontal line on a given X-coordinate range
    and of a specific Y-cooridate level.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10.0) # Set the point with a specific radius
    glBegin(GL_POINTS) # Begin plotting point
    x = x_min
    while (x <= x_max):
        glVertex2f(x, y)
        x += 0.05
    glEnd()
    glFlush()

def vline(y_min, y_max, x):
    """
    Plot vertical line on a given Y-coordinate range
    and of a specific X-cooridate level.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    y = y_min
    while (y <= y_max):
        glVertex2f(x, y)
        y += 0.05
    glEnd()
    glFlush()

def dline(x, y):
    """
    Plot diagonal line from (x, x) to (y, y).
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    while (x <= y):
        glVertex2f(x, x)
        x += 0.05
    glEnd()
    glFlush()

def main():
    choice = input("Enter Choice: ")
    if(int(choice) == 1):
        xmin = float(input("Enter x start range: "))
        xmax = float(input("Enter x end range: "))
        y = float(input("Enter Y offset: "))
        print("starting window....")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("LAB 3 | HORIZONTAL LINE")
        glutDisplayFunc(lambda: hLine(xmin,xmax,y)) # Refer RE1013 for why the use of lambda
        glutIdleFunc(lambda: hLine(xmin,xmax,y))
        initGL()
        glutMainLoop()
    elif (int(choice) == 2):
        ymin = float(input("Enter y start range: "))
        ymax = float(input("Enter y end range: "))
        x = float(input("Enter x offset: "))
        print("starting window....")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("LAB 3 | VERTICAL LINE")
        glutDisplayFunc(lambda: vline(ymin,ymax,x)) # Refer RE1013 for why the use of lambda
        glutIdleFunc(lambda: vline(ymin,ymax,x))
        initGL()
        glutMainLoop()
    elif (int(choice) == 3):
        x = float(input("Enter start cordinate(x,x) as x: "))
        y = float(input("Enter end cordinate(y,y) as y: "))
        print("starting window....")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("LAB 3 | DIAGONAL LINE")
        glutDisplayFunc(lambda: dline(x,y)) # Refer RE1013 for why the use of lambda
        glutIdleFunc(lambda: dline(x,y))
        initGL()
        glutMainLoop()
    else: 
        print("Invalid choice")

if __name__ == "__main__":
    main()
