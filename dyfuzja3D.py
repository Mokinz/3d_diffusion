import numpy as np
from random import randrange

"""Variables"""

Lp = 1  # Program Run Count
L = 3  # Side of Cube
N = 1  # Atom Quantity
MCS = 50  # Monte Carlo Steps
deltaX = np.zeros(N)
deltaY = np.zeros(N)
deltaZ = np.zeros(N)

"""Main program"""


for program_run in range(Lp):

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
    print(cube)
    print(t_cube)

    for choice in range(MCS):

        for next_atom in range(N):

            x = int(t_cube[next_atom][0])
            y = int(t_cube[next_atom][1])
            z = int(t_cube[next_atom][2])

            move = randrange(6)

            if move == 0:
                """ x + 1 """
                if x + 1 == L:
                    if cube[0][y][z] == 0:
                        cube[x][y][z] = 0
                        cube[0][y][z] = 1
                        t_cube[next_atom][0] = 0
                        deltaX[next_atom] += 1
                    else:
                        continue
                else:
                    if cube[x + 1][y][z] == 0:
                        cube[x][y][z] = 0
                        cube[x + 1][y][z] = 1
                        t_cube[next_atom][0] = x + 1
                        deltaX[next_atom] += 1
                    else:
                        continue

            elif move == 1:
                """ x - 1 """

                if x == 0:
                    if cube[L - 1][y][z] == 0:
                        cube[x][y][z] = 0
                        cube[L - 1][y][z] = 1
                        t_cube[next_atom][0] = L - 1
                        deltaX[next_atom] -= 1
                    else:
                        continue
                else:
                    if cube[x - 1][y][z] == 0:
                        cube[x][y][z] = 0
                        cube[x - 1][y][z] = 1
                        t_cube[next_atom][0] = x - 1
                        deltaX[next_atom] -= 1
                    else:
                        continue

            elif move == 2:
                """ y + 1 """

                if y + 1 == L:
                    if cube[x][0][z] == 0:
                        cube[x][y][z] = 0
                        cube[x][0][z] = 1
                        t_cube[next_atom][1] = 0
                        deltaY[next_atom] += 1
                    else:
                        continue
                else:
                    if cube[x][y + 1][z] == 0:
                        cube[x][y][z] = 0
                        cube[x][y + 1][z] = 1
                        t_cube[next_atom][1] = y + 1
                        deltaY[next_atom] += 1
                    else:
                        continue

            elif move == 3:
                """ y - 1 """

                if y == 0:
                    if cube[x][L - 1][z] == 0:
                        cube[x][y][z] = 0
                        cube[x][L - 1][z] = 1
                        t_cube[next_atom][1] = L - 1
                        deltaY[next_atom] -= 1
                    else:
                        continue
                else:
                    if cube[x][y - 1][z] == 0:
                        cube[x][y][z] = 0
                        cube[x][y - 1][z] = 1
                        t_cube[next_atom][1] = y - 1
                        deltaY[next_atom] -= 1
                    else:
                        continue

            elif move == 4:
                """ z + 1 """

                if z + 1 == L:
                    if cube[x][y][0] == 0:
                        cube[x][y][z] = 0
                        cube[x][y][0] = 1
                        t_cube[next_atom][2] = 0
                        deltaZ[next_atom] += 1
                    else:
                        continue
                else:
                    if cube[x][y][z + 1] == 0:
                        cube[x][y][z] = 0
                        cube[x][y][z + 1] = 1
                        t_cube[next_atom][2] = z + 1
                        deltaZ[next_atom] += 1
                    else:
                        continue

            else:
                """ z - 1 """

                if z == 0:
                    if cube[x][y][L - 1] == 0:
                        cube[x][y][z] = 0
                        cube[x][y][L - 1] = 1
                        t_cube[next_atom][2] = L - 1
                        deltaZ[next_atom] -= 1
                    else:
                        continue
                else:
                    if cube[x][y][z - 1] == 0:
                        cube[x][y][z] = 0
                        cube[x][y][z - 1] = 1
                        t_cube[next_atom][2] = z - 1
                        deltaZ[next_atom] -= 1
                    else:
                        continue


# print(deltaX)
# print(deltaY)
# print(deltaZ)


print(cube)
print(t_cube)
"""Functions"""
