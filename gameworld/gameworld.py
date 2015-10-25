import sys
import random
import turtle


class CWorld:
    def __init__(self, x_size, y_size):
        # Init some world constants
        self.default_color="#ffffff"
        self.bgcolor = "#ffffff"
        self.cell_color = "#333333"
        self.cell_size = 5
        self.x_size = x_size
        self.y_size = y_size
        # Continuity of simulation
        self.is_continuous = False
        self.simulation_speed = 150

        # Init the world properties
        # create a screen to draw the cells
        self.screen = turtle.Screen()
        self.screen.title("Game Of Life")
        self.__init_screen_stuff()

        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed("fastest")

        self.world_state = set()
        # catch screen click event

    def __init_screen_stuff(self):
        self.screen.bgcolor(self.bgcolor)
        self.screen.reset()
        self.screen.mode("standard")
        self.screen.delay(0)
        self.screen.tracer(0, 0)
        self.screen.onclick(self.toggle_cell_callback)
        self.screen.screensize(self.x_size * self.cell_size, self.y_size * self.cell_size)
        self.screen.setworldcoordinates(0,0,self.x_size * self.cell_size, self.y_size * self.cell_size + (self.cell_size//2))

    def bind_keys(self):
        # for Exiting
        self.screen.onkey(sys.exit, 'q')
        self.screen.onkey(self.erase_board, 'e')
        self.screen.onkey(self.fill_board_randomly, 'r')
        self.screen.onkey(self.fill_board_completely, 'f')
        self.screen.onkey(self.go_to_next_gen_automatic, 'c')
        self.screen.onkey(self.go_to_next_gen_manual, 's')
        self.screen.onkey(self.sim_speed_down, 'z')
        self.screen.onkey(self.sim_speed_up, 'a')

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

    def draw_cell(self, px, py):
        # DRAWS A SINGLE CELL AT POS(X, Y)
        self.pen.up()
        self.pen.setpos(px*self.cell_size, py*self.cell_size+self.cell_size)
        # Set heading to east - always go right so we know init state of pen
        self.pen.setheading(0)
        self.pen.pd()
        self.pen.color(self.cell_color)
        self.pen.begin_fill()

        self.pen.begin_poly()
        for i in range(4):
            self.pen.forward(self.cell_size-2)
            self.pen.right(90)
        self.pen.end_poly()
        self.pen.end_fill()
        self.pen.color(self.default_color)

    def draw_board(self):
        # REDRAWS THE ENTIRE BOARD BASED ON STATE
        self.erase_board(clear_state=False)
        for x, y in self.world_state:
            self.draw_cell(x, y)
        self.screen.update()
        # call key binding
        self.bind_keys()

    def erase_board(self, clear_state=True):
        # Clears the state - no draw code here
        if clear_state:
            self.world_state.clear()
        # clears everything...even key bindings! (stoopid but nm)
        self.screen.clear()
        self.__init_screen_stuff()

    def fill_board_completely(self):
        self.world_state.clear()
        for y in range(self.y_size):
            for x in range(self.x_size):
                cell = (x, y)
                self.world_state.add(cell)
        self.draw_board()

    def fill_board_randomly(self):
        self.world_state.clear()
        for y in range(self.y_size):
            for x in range(self.x_size):
                if random.random() > 0.5:
                    cell = (x, y)
                    self.world_state.add(cell)
        self.draw_board()

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
        if self.simulation_speed < 350:
            self.simulation_speed += 25

    def sim_speed_up(self):
        if self.simulation_speed > 25:
            self.simulation_speed -= 25

    def test_poly_circle(self,radius=50,extent_degrees=None):
        self.pen.color(self.default_color)
        self.pen.begin_poly()
        self.pen.circle(radius, extent_degrees)
        self.pen.end_poly()

    def toggle_cell(self, x, y):
        if self.is_pos_ok(x,y):
            cell = (x, y)
            # update the world state (no drawing is done here)
            if cell in self.world_state:
                self.world_state.remove(cell)
            else:
                self.world_state.add(cell)

    def toggle_cell_callback(self, x, y):
        cell_x = int(x // self.cell_size)
        cell_y = int(y // self.cell_size)
        self.toggle_cell(cell_x, cell_y)
        # fill using current world state
        self.draw_board()
