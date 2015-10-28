from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


ESCAPE = b'\033'

window = 0

#rotation vars
# for global environment
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0
# for cube 1
X_AXIS1 = 0.0
Y_AXIS1 = 0.0
Z_AXIS1 = 0.0
# for cube 2
X_AXIS2 = 0.0
Y_AXIS2 = 0.0
Z_AXIS2 = 0.0

DIRECTION = 1

FOV_ANGLE = 60.0

WIREFRAME = False



def InitGL(Width, Height):

        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(FOV_ANGLE, float(Width)/float(Height), 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)


def keyPressed(*args):
        global WIREFRAME
        if args[0] == ESCAPE:
            sys.exit()
        elif args[0] == b'w':
            #toggle wireframe mode
            print(WIREFRAME)
            WIREFRAME = not WIREFRAME


def draw_cube(wireframe=False):
    # Draw Cube (multiple quads)
    #whether or not to draw a wireframe
    if wireframe:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    else:
        glPolygonMode( GL_FRONT_AND_BACK, GL_FILL )

    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f( 1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0,-1.0)
    glVertex3f( 1.0, -1.0,-1.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f( 1.0, 1.0, -1.0)

    glColor3f(0.0,1.0,0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f( 1.0, 1.0, -1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0, -1.0, 1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glEnd()

def oneCube():
    global X_AXIS,Y_AXIS,Z_AXIS
    global DIRECTION

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    glTranslatef(0.0,0.0,-5.0)

    glRotatef(X_AXIS,1.0,0.0,0.0)
    glRotatef(Y_AXIS,0.0,1.0,0.0)
    glRotatef(Z_AXIS,0.0,0.0,1.0)

    draw_cube()

    X_AXIS = X_AXIS - 0.30
    Z_AXIS = Z_AXIS - 0.30

    glutSwapBuffers()

def DrawGLScene():
    global X_AXIS,Y_AXIS,Z_AXIS
    global X_AXIS1,Y_AXIS1,Z_AXIS1
    global X_AXIS2,Y_AXIS2,Z_AXIS2
    global DIRECTION

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Load up an identity matrix
    glLoadIdentity()


    """
    ******** First cube
    """

    glPushMatrix()
    glLoadIdentity()
    # Position of the cube in the world
    glTranslatef(0.0,0.0,-5.0)
    # Rotate by X and Z
    glRotatef(X_AXIS1,1.0,0.0,0.0)
    glRotatef(Y_AXIS1,0.0,1.0,0.0)
    glRotatef(Z_AXIS1,0.0,0.0,1.0)
    # Red color
    glColor3f(1, 0, 0);
    glutWireCube(1)
    # update angles
    X_AXIS1 = X_AXIS1 - 0.30
    Z_AXIS1 = Z_AXIS1 - 0.30
    glPopMatrix()

    """
    ******** Second cube
    """

    glPushMatrix()
    glLoadIdentity()
    # Position of the cube in the world
    glTranslatef(0.0,1.5,-5.0)
    # Rotate by X and Z
    glRotatef(X_AXIS2,1.0,0.0,0.0)
    glRotatef(Y_AXIS2,0.0,1.0,0.0)
    glRotatef(Z_AXIS2,0.0,0.0,1.0)
    # Green color (RGB)
    glColor3f(0, 1, 0);
    glutWireCube(1)
    # update angles
    X_AXIS2 = X_AXIS2 - 0.30
    Z_AXIS2 = Z_AXIS2 - 0.30
    glPopMatrix()


    # Swap in the newly drawn buffer to the front and bring the old one back to be redrawn
    glutSwapBuffers()



def main():

        global window

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640,480)
        glutInitWindowPosition(200,200)

        window = glutCreateWindow('OpenGL Python Cube')

        glutDisplayFunc(DrawGLScene)
        glutIdleFunc(DrawGLScene)
        glutKeyboardFunc(keyPressed)
        InitGL(640, 480)
        glutMainLoop()

if __name__ == "__main__":
        main()

