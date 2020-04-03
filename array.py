import random
import numpy as np
from random import randrange

Lp = 3  # Program Run Count
L = 3  # Side of Cube
N = 1  # Atom Quantity
mcs = 1000  # Monte Carlo Steps


cube = np.zeros((L, L, L))  # Creates a 3D array with filled with 0
t_cube = np.zeros((N, 3))

for atom in range(N):
    """Filling in declared amount of atoms"""

    x = randrange(L)
    y = randrange(L)  # Generates a random place
    z = randrange(L)

    if cube[x][y][z] == 1:
        while cube[x][y][z] == 1:
            x = randrange(L)
            y = randrange(L)
            z = randrange(L)
        cube[x][y][z] = 1
        t_cube[atom] = [x, y, z]
    else:
        cube[x][y][z] = 1
        t_cube[atom] = [x, y, z]
# print(cube)
# print(t_cube)

for next_atom in range(N):

    x = int(t_cube[next_atom, 0])
    y = int(t_cube[next_atom][1])
    z = int(t_cube[next_atom][2])
    # print(x)
    # print(y)
    # print(z)
print(cube[x][y][z])
