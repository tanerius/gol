import turtle

class CControlPanel:
    def __init__(self):
        from turtle import TK
        # get a handle to the master container of the canvas
        tk_hndl = TK.Tk()
        frame = TK.Frame()
        # create a new canvas to hold the control window
        self.canvas = TK.Canvas(tk_hndl, width=350, height=300, bg="#333333")
        # control the appearance of container
        self.canvas.pack()

        # Create the interaction screen
        self.interact_screen = turtle.TurtleScreen(self.canvas)
        self.interact_screen.tracer(0, 0)

        # create a raw pen to write on this screen
        self.interact_pen = turtle.RawTurtle(self.interact_screen)
        # init the pen
        self.interact_pen.pu()
        self.interact_pen.hideturtle()
        self.interact_pen.speed("fastest") # renderer speed

        w, h = self.interact_screen.screensize()
        line_height = 20
        y = h // 2 - 30

        text_for_display = (
            "Click on cells to toggle them.",
            "Options:",
            "E - Erase the board",
            "F - Fill up the board completely",
            "R - Generate a random world",
            "S - Go to next step",
            "C - Run continuously",
            "Q - Quit Game"
        )

        for l in text_for_display:
            self.interact_pen.setpos(-(w/2),y)
            self.interact_pen.write(l, font=('sans-serif', 12, 'normal'))
            # calculate next line
            y -= line_height