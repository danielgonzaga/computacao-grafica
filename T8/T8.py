import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from png import Reader
from sys import argv
from math import sin, cos, pi


name = "Trabalho 8 - Daniel Gonzaga"
alpha = 90.0
beta = 0
delta_alpha = 1.15
delta_x, delta_y, delta_z = 0, 0, 0
bgc = (0, 0, 0, 1)
n = 50
m = 50
raio = 2
texture = []


def f(i, j):
    theta = ((pi * i) / (n - 1)) - (pi / 2)
    phi = 2 * pi * j / (m - 1)
    x = raio * cos(theta) * cos(phi)
    y = raio * sin(theta)
    z = raio * cos(theta) * sin(phi)
    s = s_func(phi)
    t = t_func(theta)
    return x, y, z, s, t


def s_func(phi):
    return (phi / (2 * pi))


def t_func(theta):
    return ((theta + (pi / 2)) / pi)


def load_textures():
    global texture
    texture = GL.glGenTextures(2)
    image = Reader(filename='.\\mapa.png')
    w, h, pixels, metadata = image.read_flat()
    if metadata['alpha']:
        mode = GL.GL_RGBA
    else:
        mode = GL.GL_RGB
    GL.glBindTexture(GL.GL_TEXTURE_2D, texture[0])
    GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT, 1)
    GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, mode, w, h, 0, mode, GL.GL_UNSIGNED_BYTE, pixels.tolist())
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
    GL.glTexEnvf(GL.GL_TEXTURE_ENV, GL.GL_TEXTURE_ENV_MODE, GL.GL_DECAL)


def figure():
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glLoadIdentity()
    GL.glPushMatrix()
    GL.glTranslatef(delta_x, delta_y, delta_z)
    GL.glRotatef(alpha, 0.0, 1.0, 0.0)
    GL.glRotatef(beta, 0.0, 0.0, 1.0)
    GL.glBindTexture(GL.GL_TEXTURE_2D, texture[0])
    for i in range(n):
        GL.glBegin(GL.GL_QUAD_STRIP)
        for j in range(m):
            x, y, z, s, t = f(i, j)
            GL.glTexCoord2f(s, t)
            GL.glVertex3f(x, y, z)
            x, y, z, s, t = f(i + 1, j)
            GL.glTexCoord2f(s, t)
            GL.glVertex3f(x, y, z)
        GL.glEnd()
    GL.glPopMatrix()
    GLUT.glutSwapBuffers()


def draw():
    global alpha
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    figure()
    alpha = alpha + delta_alpha
    GLUT.glutSwapBuffers()


def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(10, timer, 1)


def main():
    GLUT.glutInit(argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_DOUBLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH | GLUT.GLUT_MULTISAMPLE)
    screen_width = GLUT.glutGet(GLUT.GLUT_SCREEN_WIDTH)
    screen_height = GLUT.glutGet(GLUT.GLUT_SCREEN_HEIGHT)
    window_width = round(2 * screen_width / 3)
    window_height = round(2 * screen_height / 3)
    GLUT.glutInitWindowSize(window_width, window_height)
    GLUT.glutInitWindowPosition(round((screen_width - window_width) / 2), round((screen_height - window_height) / 2))
    GLUT.glutCreateWindow(name)
    GLUT.glutDisplayFunc(draw)
    load_textures()
    GL.glEnable(GL.GL_MULTISAMPLE)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glEnable(GL.GL_TEXTURE_2D)
    GL.glClearColor(*bgc)
    GL.glClearDepth(1.0)
    GL.glDepthFunc(GL.GL_LESS)
    GL.glShadeModel(GL.GL_SMOOTH)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GLU.gluPerspective(-45, window_width / window_height, 0.1, 100.0)
    GL.glTranslatef(0.0, 0.0, -10)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GLUT.glutTimerFunc(10, timer, 1)
    GLUT.glutMainLoop()


if __name__ == '__main__':
    main()
