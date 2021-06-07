import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from png import Reader
from sys import argv
from math import sin, cos, pi


name = "Trabalho 7 - Daniel Gonzaga"
alpha = 90.0
beta = 0
delta_alpha = 1.15
delta_x, delta_y, delta_z = 0, 0, 0
bgc = (0, 0, 0, 1)
vertices = 5
raio = 2
altura = 5
texture = []


def load_textures():
    global texture
    texture = GL.glGenTextures(2)
    image = Reader(filename='.\\piramidetextura.png')
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
    polygon_points = []
    faces_angle = (2 * pi) / vertices
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glLoadIdentity()
    GL.glPushMatrix()
    GL.glTranslatef(0.0, 1.5, -10)
    GL.glRotatef(90, 1.0, 0.0, 0.0)
    GL.glTranslatef(delta_x, delta_y, delta_z)
    GL.glRotatef(alpha, 0.0, 0.25, 1.0)
    GL.glRotatef(beta, 0.0, 1.0, 0.0)
    GL.glBindTexture(GL.GL_TEXTURE_2D, texture[0])
    GL.glBegin(GL.GL_POLYGON)
    for i in range(vertices):
        x = raio * cos(i * faces_angle)
        y = raio * sin(i * faces_angle)
        polygon_points += [(x, y)]
        GL.glTexCoord2f(x, y);
        GL.glVertex3f(x, y, 0.0)
    GL.glEnd()
    GL.glBegin(GL.GL_POLYGON)
    for x, y in polygon_points:
        GL.glTexCoord2f(x, y);
        GL.glVertex3f(0.5 * x, 0.5 * y, altura)
    GL.glEnd()
    GL.glBegin(GL.GL_QUADS)
    for i in range(vertices):
        GL.glTexCoord2f(0.0, 0.0);
        GL.glVertex3f(polygon_points[i][0], polygon_points[i][1], 0)
        GL.glTexCoord2f(0.0, 1.0);
        GL.glVertex3f(0.5 * polygon_points[i][0], 0.5 * polygon_points[i][1], altura)
        GL.glTexCoord2f(1.0, 1.0);
        GL.glVertex3f(0.5 * polygon_points[(i + 1) % vertices][0],
                      0.5 * polygon_points[(i + 1) % vertices][1], altura)
        GL.glTexCoord2f(1.0, 0.0);
        GL.glVertex3f(polygon_points[(i + 1) % vertices][0], polygon_points[(i + 1) % vertices][1], 0)
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
    GL.glTranslatef(0.0, 0.0, -3)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GLUT.glutTimerFunc(10, timer, 1)
    GLUT.glutMainLoop()


if __name__ == '__main__':
    main()
