#!/usr/bin/python
# Conway's Game of Life Simulation v1.0 (python 3)
# Entry point
#
# Copyright (C) 2015  Taner Selim <tanerius@gmail.com>

"""
    Rules:
    1. Any cell with fewer than 2 neighbours dies (under-population)
    2. Any cell with 2 or 3 neighbours lives on (survival)
    3. Any cell with more than 3 neighbours dies (overcrowding)
    4. Any DEAD cell with exactly 3 live neighbours becomes alive (reproduction)
"""

import argparse
import turtle
from gamepanel.gamepanel import CControlPanel
from gameworld.gameworld import CWorld

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'gol.py',
        description = 'Runs a (TK rendered) simulation of Conway\'s Game of Life')

    parser.add_argument('xsize', metavar='X_size', type=int,
                   help='an integer for the size of X', default=25)
    parser.add_argument('ysize', metavar='y_size', type=int,
                   help='an integer for the size of y', default=25)

    args = parser.parse_args()

    # Make a control pane
    control_pane = CControlPanel()
    # Make a world
    world = CWorld(args.xsize, args.ysize)
    # Fill it randomly
    world.fill_board_randomly()

    # Start the main loop
    turtle.listen()
    turtle.mainloop()
