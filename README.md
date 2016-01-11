# Conway's Game of Life

A Python implementation of Conway's Game Of Life (simulation) using OpenGL

## Simulation Rules
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells,
each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours,
which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by over-population.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules
simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete moment at which this
happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one).
The rules continue to be applied repeatedly to create further generations.

Go to the [Wikipedia: Game Of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) page for more info.

## Module requirements

Modules needed for the simulation to work are:
 - PyOpenGL==3.1.0

Either install them with:

pip install PyOpenGL PyOpenGL_accelerate
or
sudo apt-get install python_opengl

## TODO
### World in 3D
I'll eventually expand this to a 3D simulation, where the world would be cube for instance.
### More rules
I was also thinking of adding additional features like ability to add more rules just to see the outcome