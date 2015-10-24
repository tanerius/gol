import turtle

class CWorld:
    def __init__(self,x_size,y_size):
        # Init some world constants
        self.default_color="#333333"
        self.bgcolor = "#333333"
        self.cell_color = "#888888"
        self.cell_size = 5
        self.x_size = x_size
        self.y_size = y_size

        # Init the world properties
        self.screen = turtle.Screen()
        self.screen.mode("standard")
        self.screen.tracer(0, 0)
        self.screen.bgcolor(self.bgcolor)
        self.screen.title("Game Of Life")
        #self.screen.reset()

        self.screen.screensize(self.x_size * self.cell_size, self.y_size * self.cell_size)
        self.screen.setworldcoordinates(0,0,self.x_size * self.cell_size, self.y_size * self.cell_size + (self.cell_size//2))

        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed("fastest")

        self.world_state = set()
        # catch screen click event
        self.screen.onclick(self.toggle_cell_callback)

    def draw_board(self):
        self.screen.clear()
        for x,y in self.world_state:
            self.draw_cell(x, y)
        self.screen.update()

    def draw_cell(self,px, py):
        # draws a single cell at position x,y
        self.pen.up()
        self.pen.setpos(px*self.cell_size,py*self.cell_size+self.cell_size)
        self.pen.setheading(0) # Set heading to east - always go right so we know init state of pen
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

    def erase_board(self):
        # Clears the state - no draw code here
        print('Erase board')
        self.world_state.clear()
        print(self.world_state)
        self.draw_board()

    def fill_board(self):
        self.screen.clear()
        for y in range(self.y_size):
            for x in range(self.x_size):
                self.draw_cell(x, y)
                cell = (x,y)
                self.world_state.add(cell)
        self.screen.update()

    @property
    def get_state(self):
        return self.world_state

    def is_pos_ok(self,x,y):
        # test if position is ok to have a cell in (is within world bounds)
        return ( 0 <= x < self.x_size) and (0 <= y < self.y_size)

    def test_poly_circle(self,radius=50,extent_degrees=None):
        self.pen.color(self.default_color)
        self.pen.begin_poly()
        self.pen.circle(radius, extent_degrees)
        self.pen.end_poly()

    def toggle_cell(self,x,y):
        if self.is_pos_ok(x,y):
            print('Position is OK')
            cell = (x, y)
            # update the world state (no drawing is done here)
            if cell in self.world_state:
                self.world_state.remove(cell)
            else:
                self.world_state.add(cell)

    def toggle_cell_callback(self,x,y):
        cell_x = x // self.cell_size
        cell_y = y // self.cell_size
        print('Toggle ('+str(cell_x)+','+str(cell_y)+')')
        self.toggle_cell(cell_x, cell_y)
        self.draw_board()