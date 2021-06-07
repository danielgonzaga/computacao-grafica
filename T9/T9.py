import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi, sqrt


name = "Trabalho 9 - Daniel Gonzaga"
bgc = (255, 255, 255, 1)
vertices = 5
raio = 3
altura = 4
X = 0
Y = 1
Z = 2
counter = 0
materials = [
    # Red rubber
    [
        (0.05, 0.0, 0.0, 1.0),
        (0.5, 0.4, 0.4, 1.0),
        (0.7, 0.04, 0.04, 1.0),
        (10.0)
    ]
]


def normal_calculation(v0, v1, v2, sign):
    u = (v2[X] - v0[X], v2[Y] - v0[Y], v2[Z] - v0[Z])
    v = (v1[X] - v0[X], v1[Y] - v0[Y], v1[Z] - v0[Z])
    n = ((u[Y] * v[Z] - u[Z] * v[Y]), (u[Z] * v[X] - u[X] * v[Z]), (u[X] * v[Y] - u[Y] * v[X]))
    length = sqrt(n[X] * n[X] + n[Y] * n[Y] + n[Z] * n[Z])
    if sign == 1:
        return n[X] / length, n[Y] / length, n[Z] / length
    elif sign == 0:
        return -n[X] / length, -n[Y] / length, -n[Z] / length


def figure():
    polys = []
    angles = (2 * pi) / vertices
    GL.glPushMatrix()
    GL.glTranslatef(0.0, -1.0, 0.0)
    GL.glRotatef(-100, 1.0, 0.0, 0.0)
    GL.glBegin(GL.GL_POLYGON)
    for i in range(vertices):
        x = raio * cos(i * angles)
        y = raio * sin(i * angles)
        polys += [(x, y)]
        GL.glVertex3f(x, y, 0.0)
    u = (polys[0][0], polys[0][1], 0)
    v = (polys[1][0], polys[1][1], 0)
    p = (polys[2][0], polys[2][1], 0)
    GL.glNormal3fv(normal_calculation(u, v, p, 0))
    GL.glEnd()
    GL.glBegin(GL.GL_POLYGON)
    for x, y in polys:
        GL.glVertex3f(0.5 * x, 0.5 * y, altura)
    u = (polys[0][0], polys[0][1], altura)
    v = (polys[1][0], polys[1][1], altura)
    p = (polys[2][0], polys[2][1], altura)
    GL.glNormal3fv(normal_calculation(u, v, p, 1))
    GL.glEnd()
    GL.glBegin(GL.GL_QUADS)
    for i in range(vertices):
        u = (polys[i][0], polys[i][1], 0)
        v = (0.5 * polys[i][0], 0.5 * polys[i][1], altura)
        p = (0.5 * polys[(i + 1) % vertices][0],
             0.5 * polys[(i + 1) % vertices][1], altura)
        q = (polys[(i + 1) % vertices][0], polys[(i + 1) % vertices][1], 0)
        GL.glNormal3fv(normal_calculation(u, v, q, 1))
        GL.glVertex3fv(u)
        GL.glVertex3fv(v)
        GL.glVertex3fv(p)
        GL.glVertex3fv(q)
    GL.glEnd()
    GL.glPopMatrix()


def draw():
    global counter
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glRotatef(6, 1, 3, 0)
    if counter % 150 == 0:
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_AMBIENT, materials[(counter + 1) % len(materials)][0])
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_DIFFUSE, materials[(counter + 1) % len(materials)][1])
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_SPECULAR, materials[(counter + 1) % len(materials)][2])
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_SHININESS, materials[(counter + 1) % len(materials)][3])
    counter += 1
    figure()
    GLUT.glutSwapBuffers()


def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(50, timer, 1)


def reshape(w, h):
    GL.glViewport(0, 0, w, h)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GLU.gluPerspective(45, float(w) / float(h), 0.1, 50.0)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()
    GLU.gluLookAt(10, 0, 0, 0, 0, 0, 0, 1, 0)


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
    GLUT.glutReshapeFunc(reshape)
    GLUT.glutDisplayFunc(draw)
    GL.glShadeModel(GL.GL_SMOOTH)
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_AMBIENT, materials[0][0])
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_DIFFUSE, materials[0][1])
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_SPECULAR, materials[0][2])
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_SHININESS, materials[0][3])
    pos_light = (10, 0, 0)
    GL.glEnable(GL.GL_LIGHTING)
    GL.glEnable(GL.GL_LIGHT0)
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, pos_light)
    GL.glEnable(GL.GL_MULTISAMPLE)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearColor(*bgc)
    GLU.gluPerspective(45, window_width / window_height, 0.1, 50.0)
    GLUT.glutTimerFunc(50, timer, 1)
    GLUT.glutMainLoop()


if __name__ == '__main__':
    main()
