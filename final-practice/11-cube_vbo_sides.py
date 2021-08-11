from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

vertex_src = """
# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;
// uniform mat4 model_view;
uniform mat4 projection;
out vec3 v_color;
void main()
{
    gl_Position = projection * vec4(a_position, 1.0);
    v_color = vec3(1.0, 0.0, 0.0);
}
"""

fragment_src = """
# version 330
in vec3 v_color;
out vec4 out_color;
void main()
{
    out_color = vec4(v_color, 1.0);
}
"""

# perspectiveMatrix = np.array([
#     [2.4142, 0.0000, 0.0000, 0.0000],
#     [0.0000, 2.4142, 0.0000, 0.0000],
#     [0.0000, 0.0000, -1.0020, -0.2002],
#     [0.0000, 0.0000, -1.0000, 0.0000],
# ])

perspectiveMatrix = np.array([
    [np.sqrt(2)/4, -np.sqrt(2)/2, 0, 0],
    [0.5, 0.25, -np.sqrt(2)/2, 0],
    [0.5, 0.5, np.sqrt(2)/4, 0],
    [0, 0, 0, 1]
])

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    vertices = [
        -0.5 , 0.5 , 0.5,
        -0.5 , 0.5 , -0.5,
        -0.5 ,-0.5 , 0.5,
        -0.5, -0.5, -0.5,

        0.5, -0.5, 0.5,
        0.5, -0.5, -0.5,
        0.5, 0.5, 0.5,
        0.5, 0.5, -0.5,

        -0.5 , 0.5 , 0.5,
        -0.5 , 0.5 , -0.5,
    ]

    indices = [0,1,2,3,4,5,6,7,8,9]

    vertices = np.array(vertices, dtype=np.float32)
    indices = np.array(indices, dtype=np.uint32)

    shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

    # Vertex Buffer Object
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # Element Buffer Object
    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))

    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(12))

    glUseProgram(shader)

    transformLoc = glGetUniformLocation(shader, "projection")
    glUniformMatrix4fv(transformLoc, 1, GL_FALSE, perspectiveMatrix)

    glDrawElements(GL_TRIANGLE_STRIP, len(indices), GL_UNSIGNED_INT, None)

    # Draw points
    glPointSize(6.0)
    glBegin(GL_POINTS)
    for i in range(0, len(vertices), 3):
        glVertex3f(vertices[i], vertices[i+1], vertices[i+2])
    glEnd()

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("PyOpenGL | LAB 11")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()