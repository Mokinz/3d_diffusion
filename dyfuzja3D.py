import numpy as np
from random import randrange
from tqdm import tqdm
from math import pow

"""Inputs"""

# Program Run Count
Lp = int(input("Results accuracy (If you don't know, we recommend 20): "))
if Lp < 1:
    while Lp < 1:
        Lp = int(input("This factor can't be lower than one. Please, enter it again: "))

# Side of Cube
L = int(input("Size of the side of cube: "))
if L < 1:
    while L < 1:
        L = int(input("This factor can't be lower than one. Please, enter it again: "))

# Atom Quantity
N = int(input("Atom Quantity: "))
if N > pow(L, 3):
    while N > pow(L, 3):
        N = int(
            input("This factor can't be greater than L^3. Please, enter it again: ")
        )

# Monte Carlo Steps
mcs = int(input("Monte Carlo Steps: "))
if mcs < 1:
    while mcs < 1:
        mcs = int(
            input("This factor can't be lower than one. Please, enter it again: ")
        )

# Accuracy means that how many of last indexes are taken to calculate average D for system
average = int(input("Accuracy of avarage: "))
if average < 1:
    while average < 1:
        average = int(
            input("This factor can't be lower than one. Please, enter it again: ")
        )

"""Variables"""
# Average from all program runs (Lp) for each step
Dsr = np.zeros(mcs)
# Average from last X indexes
D_stabilised = 0


"""---!!!Main program!!!---"""

print("Calculating:")

# Program Run Loop
for program_run in tqdm(range(Lp)):
    """Runs whole program Lp times"""

    # Creates a 3D(cube) array with filled with 0
    cube = np.zeros((L, L, L))
    # An array which keeps each atom's location
    t_cube = np.zeros((N, 3))
    # Arrays that keep absolute value of each atom
    deltaX = np.zeros(N)
    deltaY = np.zeros(N)
    deltaZ = np.zeros(N)
    # Keeps a Diffiusion factor for every step the system makes
    D_step = np.zeros(mcs)

    # Generate Atoms Loop
    for atom in range(N):
        """Filling in atoms in the cube"""

        # Generates a random place
        x = randrange(L)
        y = randrange(L)
        z = randrange(L)

        # Places an atoms in generated place if it's empty and memorise it- if not - looks for another
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

    # Step Loop
    for choice in range(mcs):
        """Each iteration atom make a step in random direction"""

        # Physics factor
        R2 = 0

        # Next Atom Loop
        for next_atom in range(N):
            """Choose the next atom from the list"""

            x = int(t_cube[next_atom][0])
            y = int(t_cube[next_atom][1])
            z = int(t_cube[next_atom][2])

            # Let it "choose" by generaiting random runber
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
                    if cube[x + 1][y][z] == 0:
                        cube[x][y][z] = 0
                        cube[x + 1][y][z] = 1
                        t_cube[next_atom][0] = x + 1
                        deltaX[next_atom] += 1

            elif move == 1:
                """ x - 1 """

                if x == 0:
                    if cube[L - 1][y][z] == 0:
                        cube[x][y][z] = 0
                        cube[L - 1][y][z] = 1
                        t_cube[next_atom][0] = L - 1
                        deltaX[next_atom] -= 1

                else:
                    if cube[x - 1][y][z] == 0:
                        cube[x][y][z] = 0
                        cube[x - 1][y][z] = 1
                        t_cube[next_atom][0] = x - 1
                        deltaX[next_atom] -= 1

            elif move == 2:
                """ y + 1 """

                if y + 1 == L:
                    if cube[x][0][z] == 0:
                        cube[x][y][z] = 0
                        cube[x][0][z] = 1
                        t_cube[next_atom][1] = 0
                        deltaY[next_atom] += 1

                else:
                    if cube[x][y + 1][z] == 0:
                        cube[x][y][z] = 0
                        cube[x][y + 1][z] = 1
                        t_cube[next_atom][1] = y + 1
                        deltaY[next_atom] += 1

            elif move == 3:
                """ y - 1 """

                if y == 0:
                    if cube[x][L - 1][z] == 0:
                        cube[x][y][z] = 0
                        cube[x][L - 1][z] = 1
                        t_cube[next_atom][1] = L - 1
                        deltaY[next_atom] -= 1

                else:
                    if cube[x][y - 1][z] == 0:
                        cube[x][y][z] = 0
                        cube[x][y - 1][z] = 1
                        t_cube[next_atom][1] = y - 1
                        deltaY[next_atom] -= 1

            elif move == 4:
                """ z + 1 """

                if z + 1 == L:
                    if cube[x][y][0] == 0:
                        cube[x][y][z] = 0
                        cube[x][y][0] = 1
                        t_cube[next_atom][2] = 0
                        deltaZ[next_atom] += 1

                else:
                    if cube[x][y][z + 1] == 0:
                        cube[x][y][z] = 0
                        cube[x][y][z + 1] = 1
                        t_cube[next_atom][2] = z + 1
                        deltaZ[next_atom] += 1

            else:
                """ z - 1 """

                if z == 0:
                    if cube[x][y][L - 1] == 0:
                        cube[x][y][z] = 0
                        cube[x][y][L - 1] = 1
                        t_cube[next_atom][2] = L - 1
                        deltaZ[next_atom] -= 1

                else:
                    if cube[x][y][z - 1] == 0:
                        cube[x][y][z] = 0
                        cube[x][y][z - 1] = 1
                        t_cube[next_atom][2] = z - 1
                        deltaZ[next_atom] -= 1

        # R2 Loop
        for next_atom in range(N):
            """Calculate a R2 factor"""

            R2 = R2 + (
                pow(int(deltaX[next_atom]), 2)
                + pow(int(deltaY[next_atom]), 2)
                + pow(int(deltaZ[next_atom]), 2)
            )

        # Saves and calculates an average
        D_step[choice] = R2 / 6 / (choice + 1) / N
        Dsr[choice] = Dsr[choice] + D_step[choice] / Lp

# Average D Loop
for i in range(average):
    """Calculates average D factor for the system"""

    D_stabilised = D_stabilised + Dsr[-i] / average


print("Saving data to file:")
f = open("results.txt", "w")

# Saving Data Loop
for i in tqdm(range(mcs)):

    val = str(i + 1) + "\t" + str(Dsr[i]) + "\n"
    f.write(val)
f.close()
print("Done!")
print("Average diffusion factor: " + str(D_stabilised))
