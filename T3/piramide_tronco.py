from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5))


def tronco():
    raio_maior = 2
    raio_menor = 1.2
    base_maior = []
    base_menor = []
    N = 5
    H = 4
    angulo = (2 * math.pi) / N

    glPushMatrix()
    glTranslatef(0, -2, 0)
    glRotatef(a, 0.0, 1.0, 0.0)
    glRotatef(-110, 1.0, 0.0, 0.0)
    glColor3fv(cores[0])

    # BASE INFERIOR (MAIOR)
    glBegin(GL_POLYGON)
    for i in range(0, N):
        x = raio_maior * math.cos(i*angulo)
        y = raio_maior * math.sin(i*angulo)
        base_maior += [(x, y)]
        glVertex3f(x, y, 0.0)
    glEnd()

    # BASE SUPERIOR (MENOR)
    glBegin(GL_POLYGON)
    for i in range(0, N):
        x = raio_menor * math.cos(i*angulo)
        y = raio_menor * math.sin(i*angulo)
        base_menor += [(x, y)]
        glVertex3f(x, y, H)
    glEnd()

    # LATERAIS
    glBegin(GL_TRIANGLES)

    # PERCORRENDO LATERAIS
    for i in range(0, N):
        glColor3fv(cores[(i+1) % len(cores)])
        
        glVertex3f(base_maior[i][0], base_maior[i][1], 0.0)
        glVertex3f(base_maior[(i+1) % N][0], base_maior[(i+1) % N][1], 0.0)
        glVertex3f(base_menor[i][0], base_menor[i][1], H)
    
        glVertex3f(base_menor[i][0], base_menor[i][1], H)
        glVertex3f(base_menor[(i+1) % N][0], base_menor[(i+1) % N][1], H)
        glVertex3f(base_maior[(i+1) % N][0], base_maior[(i+1) % N][1], 0)
       
    glEnd()

    glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    tronco()
    a += 1
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0, 0, 0, 1)
gluPerspective(45, 800.0/600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -10)
glutTimerFunc(10, timer, 1)
glutMainLoop()
