import random
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



class CWorldGl:
    def __init__(self, x_size, y_size):
        # Init some world constants
        self.default_color="#ffffff"
        self.bgcolor = (0.9, 0.9, 0.9)
        self.cell_color = (0.3, 0.3, 0.3)
        self.cell_size = 10
        self.x_size = x_size
        self.y_size = y_size
        # Continuity of simulation
        self.is_continuous = False
        self.simulation_speed = 150
        self.title = "Game Of Life - OpenGL Edition"
        self.world_state = set()
        self.window = None
        self.fill_board_randomly()
        self.do_step = False
        self.timestamp = 0
        self.__init_opengl()

    def __init_gl_2d(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity()

    def __init_opengl(self):
        glutInit()                                                              # initialize glut
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)  # display mode
        glutInitWindowSize(self.x_size * self.cell_size, self.y_size * self.cell_size)                            # set window size
        glutInitWindowPosition(50, 50)                                            # set window initial position
        self.window = glutCreateWindow(self.title)                              # create window with title
        glutKeyboardFunc(self.callback_bind_keys)                               # kb event callback
        glutMouseFunc(self.callback_mouse_handler)                              # mouse event callback
        glutDisplayFunc(self.draw_board)                                        # set draw function callback
        glutIdleFunc(self.draw_board)                                           # draw all the time
        glutMainLoop()                                                          # start everything

    def callback_bind_keys(self, *args):
        # for Exiting
        if args[0] in (b'\x1b', b'q'):
            sys.exit()
        elif args[0] == b'e':
            self.erase_board()
        elif args[0] == b'r':
            self.fill_board_randomly()
        elif args[0] == b'f':
            self.fill_board_completely()
        elif args[0] == b'z':
            self.sim_speed_down()
        elif args[0] == b'a':
            self.sim_speed_up()
        elif args[0] == b's':
            self.do_step = True
            self.is_continuous = False
        elif args[0] == b'c':
            self.do_step = False
            self.is_continuous = True


    def callback_mouse_handler(self, button, state, x, y):
        # Catch only mouse down event (state == 0 )
        if (state == 0) and (button==0):
            cell_x = int(x // self.cell_size)
            cell_y = self.y_size - int(y // self.cell_size) - 1
            if self.is_pos_ok(cell_x, cell_y):
                cell = (cell_x, cell_y)
                # update the world state (no drawing is done here)
                if cell in self.world_state:
                    self.world_state.remove(cell)
                else:
                    self.world_state.add(cell)
        elif (state == 0) and (button == 2):
            print('is_continuous = '+ str(self.is_continuous))
            print('do_step = '+ str(self.do_step))
            print('sim speed = '+ str(self.simulation_speed))


    def compute_next_generation(self):
        next_gen = set()
        for i in range(self.x_size):
            xrange = range(max(0, i-1),min(self.x_size, i+2))
            for j in range(self.y_size):
                live_neighbours = 0
                # get a live cell
                is_live = ((i, j) in self.world_state)
                for yp in range(max(0, j-1), min(self.y_size, j+2)):
                    for xp in xrange:
                        if (xp, yp) in self.world_state:
                            # Live neighbour
                            live_neighbours += 1
                # If live is a live cell subtract it from s since we shouldn't count it
                live_neighbours -= is_live
                # Check rules
                if live_neighbours == 3:
                    # reproduction
                    next_gen.add((i, j))
                elif (live_neighbours == 2) and is_live:
                    # survival
                    next_gen.add((i, j))
                elif is_live:
                    # death
                    pass

        self.world_state = next_gen

    def draw_cell(self, xp, yp):
        # DRAWS A SINGLE CELL AT POS(X, Y)
        x = xp * self.cell_size
        y = yp * self.cell_size
        glBegin(GL_QUADS)                                   # start drawing a rectangle
        glVertex2f(x, y)                                    # bottom left point
        glVertex2f(x + self.cell_size - 1, y)                   # bottom right point
        glVertex2f(x + self.cell_size -1, y + self.cell_size - 1)  # top right point
        glVertex2f(x, y + self.cell_size - 1)                   # top left point
        glEnd()

    def draw_board(self):
        # SOme magic to control the redraw speed on awesome graphics like mine :)
        et = glutGet(GLUT_ELAPSED_TIME)

        if (et - self.timestamp > self.simulation_speed) and self.is_continuous:
            self.timestamp = et
            self.compute_next_generation()
        elif (not self.is_continuous) and self.do_step:
            self.do_step = False
            self.is_continuous = False
            self.compute_next_generation()
        # REDRAWS THE ENTIRE BOARD BASED ON STATE
        glClearColor(self.bgcolor[0], self.bgcolor[1], self.bgcolor[2], 1.0)    # set background color
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                      # clear the screen
        glLoadIdentity()                                                        # reset position
        self.__init_gl_2d(self.x_size * self.cell_size, self.y_size * self.cell_size)                             # Set mode for 2d drawing (orthogonal)
        # Draw Cells
        glColor3f(self.cell_color[0], self.cell_color[1], self.cell_color[2])   # set cell color

        for x, y in self.world_state:
            self.draw_cell(x, y)                                                   # draw a cell
        glutSwapBuffers()                                                       # swaps to next buffer (because of GLUT_DOUBLE)
                                                                                 # swaps to next buffer (because of GLUT_DOUBLE)


    def erase_board(self):
        # Clears the state - no draw code here
        self.world_state.clear()

    def fill_board_completely(self):
        self.world_state.clear()
        for y in range(self.y_size):
            for x in range(self.x_size):
                cell = (x, y)
                self.world_state.add(cell)

    def fill_board_randomly(self):
        self.world_state.clear()
        for y in range(self.y_size):
            for x in range(self.x_size):
                if random.random() > 0.5:
                    cell = (x, y)
                    self.world_state.add(cell)


    @property
    def get_state(self):
        return self.world_state

    def go_to_next_gen(self):
        self.compute_next_generation()
        self.draw_board()
        if self.is_continuous:
            self.screen.ontimer(self.go_to_next_gen, self.simulation_speed)

    def go_to_next_gen_automatic(self):
        self.is_continuous = True
        self.go_to_next_gen()

    def go_to_next_gen_manual(self):
        self.is_continuous = False
        self.go_to_next_gen()

    def is_pos_ok(self,x,y):
        # test if position is ok to have a cell in (is within world bounds)
        return ( 0 <= x < self.x_size) and (0 <= y < self.y_size)

    def sim_speed_down(self):
        if self.simulation_speed < 1500:
            self.simulation_speed += 50

    def sim_speed_up(self):
        if self.simulation_speed > 0:
            self.simulation_speed -= 50

    def toggle_cell(self, x, y):
        if self.is_pos_ok(x,y):
            cell = (x, y)
            # update the world state (no drawing is done here)
            if cell in self.world_state:
                self.world_state.remove(cell)
            else:
                self.world_state.add(cell)
