import sys # for exitting
import turtle
from gamepanel.gamepanel import CControlPanel
from gameworld.gameworld import CWorld

class CGameOfLife:
    def __init__(self, sizex, sizey):
        # Make a control pane
        self.control_pane = CControlPanel()
        # Make a world
        self.world = CWorld(sizex, sizey)

        self.world.fill_board()
        self.bind_keys()

        # Main loop
        turtle.listen()
        turtle.mainloop()

    def bind_keys(self):
        # for Exitting
        turtle.onkey(sys.exit, 'q')
        turtle.onkey(self.world.erase_board, 'e')
