from sys import argv
import OpenGL.GLUT as GLUT
import OpenGL.GL as GL
import OpenGL.GLU as GLU


name = "Trabalho 4 - Daniel Gonzaga"
alpha = 50.0
beta = 45.0
delta_alpha = 2
delta_x, delta_y, delta_z = 0, 0, 0

bgc = (0, 0, 0, 1.5)

m, n = 100, 100
x0, y0 = -1.75, -1.75
xf, yf = 1.75, 1.75
dx, dy = (xf - x0) / m, (yf - y0) / n


def func(x, y):
    return x ** 2 - y ** 2


def figure():
    GL.glPushMatrix()
    GL.glTranslatef(delta_x, delta_y, delta_z)
    GL.glRotatef(alpha, 0.0, 1.0, 0.0)
    GL.glRotatef(beta, 0.0, 0.0, 1.0)
    for i in range(0, n):
        y = y0 + i * dy
        GL.glColor3f(1 - (i / n), 1, i / n)
        GL.glBegin(GL.GL_QUAD_STRIP)
        for j in range(0, m):
            x = x0 + j * dx
            GL.glVertex3f(x, y, func(x, y))
            GL.glVertex3f(x, y + dy, func(x, y + dy))
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
GL.glTranslatef(0.0, 0.0, -10)

GLUT.glutTimerFunc(10, timer, 1)
GLUT.glutMainLoop()
