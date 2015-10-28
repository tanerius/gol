from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

class CWorldGl3D:
    def __init__(self,width=500,height=500):
        self.__fovy = 40                        #degrees
        self.__aspect_ratio = width/height

        # initialize graphics
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutCreateWindow("red 3D lighted cube")
        glutDisplayFunc(self.callback_display)
        self.__init3D()
        glutMainLoop();


    def __init3D(self):
        # Initialize the rendering stuff
        # Enable a single OpenGL light.
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 0.0, 0.0, 1.0])           # Red diffuse light
        glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.0])          # Infinite light location
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        # Use depth buffering for hidden surface elimination
        glEnable(GL_DEPTH_TEST)
        # Setup the view of the cube.
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.__fovy, self.__aspect_ratio, 1.0,10.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # camera positioning
        gluLookAt(0.0, 0.0, 5.0,    # eye position
            0.0, 0.0, 0.0,          # center is at
            0.0, 1.0, 0.0)          # up is (positive y)
        # Adjust cube position to be asthetic angle
        glTranslatef(0.0, 0.0, -1.0)
        glRotatef(60, 1.0, 0.0, 0.0)
        glRotatef(-20, 0.0, 0.0, 1.0)

    def callback_display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw_cube()
        glutSwapBuffers()

    def draw_cube(wireframe=False):
        # Draw Cube (multiple quads)
        #whether or not to draw a wireframe
        """
        if wireframe:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode( GL_FRONT_AND_BACK, GL_FILL )
        """
        glBegin(GL_QUADS)
        glVertex3f( 1.0, 1.0,-1.0)
        glVertex3f(-1.0, 1.0,-1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f( 1.0, 1.0, 1.0)

        glVertex3f( 1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0,-1.0)
        glVertex3f( 1.0, -1.0,-1.0)

        glVertex3f( 1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0,-1.0, 1.0)
        glVertex3f( 1.0,-1.0, 1.0)

        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f( 1.0, 1.0, -1.0)

        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)

        glVertex3f( 1.0, 1.0, -1.0)
        glVertex3f( 1.0, 1.0, 1.0)
        glVertex3f( 1.0, -1.0, 1.0)
        glVertex3f( 1.0, -1.0, -1.0)
        glEnd()

    def get_normal_vector(self, v1, v2, v3):
        v = np.cross(v2-v1, v3-v1)
        n = np.sqrt(np.dot(v, v.conj()))
        if n:
            return v/n
        else:
            print(v1)
            print(v2)
            print(v3)
            print(v/n)
            sys.exit(-1)

x= CWorldGl3D()
