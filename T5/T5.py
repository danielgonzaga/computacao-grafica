import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi


name = "Trabalho 5 - Daniel Gonzaga"
alpha = 20.0
beta = 120.0
delta_alpha = 2
delta_x, delta_y, delta_z = 0, 0, 0

bgc = (0.184, 0.211, 0.250, 1)

m, n = 20, 20
r = 2


def func(i, j):
    theta = ((pi * i) / (m - 1)) - (pi / 2)
    phi = 2 * pi * j / (n - 1)

    x = r * cos(theta) * cos(phi)
    y = r * sin(theta)
    z = r * cos(theta) * sin(phi)

    return x, y ** 2, z


def figure():
    GL.glPushMatrix()
    GL.glTranslatef(delta_x, delta_y + 1.5, delta_z)
    GL.glRotatef(alpha, 0.0, 1.0, 0.0)
    GL.glRotatef(beta, 0.0, 0.0, 1.0)
    for i in range(round(m / 2)):
        GL.glBegin(GL.GL_QUAD_STRIP)
        for j in range(n):
            GL.glColor3fv(((1.0 * i / (m - 1)), 1, 1 - (1.0 * i / (m - 1))))
            x, y, z = func(i, j)
            GL.glVertex3f(x, y, z)
            GL.glColor3fv(((1.0 * (i + 1) / (m - 1)), 1, 1 - (1.0 * (i + 1) / (m - 1))))
            x, y, z = func(i + 1, j)
            GL.glVertex3f(x, y, z)
        GL.glEnd()
    GL.glPopMatrix()


def draw():
    global alpha
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    figure()
    alpha = alpha + delta_alpha
    GLUT.glutSwapBuffers()


def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(10, timer, 1)


GLUT.glutInit(argv)
GLUT.glutInitDisplayMode(
    GLUT.GLUT_DOUBLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH | GLUT.GLUT_MULTISAMPLE
)

screen_width = GLUT.glutGet(GLUT.GLUT_SCREEN_WIDTH)
screen_height = GLUT.glutGet(GLUT.GLUT_SCREEN_HEIGHT)

window_width = round(2 * screen_width / 3)
window_height = round(2 * screen_height / 3)

GLUT.glutInitWindowSize(window_width, window_height)
GLUT.glutInitWindowPosition(round((screen_width - window_width) / 2), round((screen_height - window_height) / 2))
GLUT.glutCreateWindow(name)

GLUT.glutDisplayFunc(draw)

GLU.gluPerspective(-45, window_width / window_height, 0.1, 100.0)
GL.glTranslatef(0.0, -1.0, -10)

GLUT.glutTimerFunc(10, timer, 1)
GLUT.glutMainLoop()
