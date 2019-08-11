import random
import os
import time


def initialize():
    s = input("Seed, or generate a (r)andom pattern? ")
    grid = []
    if s == "r":
        s = input("Write pattern to file?  Enter filename, or (n) if not: ")
        if s != "n":
            os.makedirs("out", exist_ok=True)
            f = open("out/{}.txt".format(s), "w")
        for _ in range(50):
            l = [random.choice([0, 1]) for _ in range(50)]
            if s != "n":
                f.write("".join([str(i) for i in l]) + "\n")
            grid.append(l)
        if s != "n":
            f.close()

    else:
        with open("in/{}.txt".format(s), "r") as f:
            for line in f:
                l = [int(line[i]) for i in range(len(line.strip()))]
                grid.append(l)
    return grid


def redraw(grid, init=False):
    alive = False
    _ = os.system("cls")
    m = {0: " ", 1: chr(9632)}
    if not init:
        grid = recompute(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            c = grid[i][j]
            if c == 1:
                alive = True
            print(m[c], end="")
        print("\n", end="")
    return grid, alive


def recompute(grid):
    copy = [[i for i in row] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid)):
            neighbors = 0
            x, y = i - 1, j - 1
            if x > -1 and y > -1:
                neighbors += grid[x][y]
            x, y = i - 1, j
            if x > -1:
                neighbors += grid[x][y]
            x, y = i - 1, j + 1
            if x > -1 and y < len(grid):
                neighbors += grid[x][y]
            x, y = i, j - 1
            if y > -1:
                neighbors += grid[x][y]
            x, y = i, j + 1
            if y < len(grid):
                neighbors += grid[x][y]
            x, y = i + 1, j - 1
            if x < len(grid) and y > -1:
                neighbors += grid[x][y]
            x, y = i + 1, j
            if x < len(grid):
                neighbors += grid[x][y]
            x, y = i + 1, j + 1
            if x < len(grid) and y < len(grid):
                neighbors += grid[x][y]
            # rules of game
            if neighbors > 3:
                copy[i][j] = 0
            elif neighbors < 2:
                copy[i][j] = 0
            elif neighbors == 2 and grid[i][j] == 0:
                copy[i][j] = 0
            else:
                copy[i][j] = 1

    return copy


if __name__ == "__main__":
    generations = -1
    alive = True

    grid = initialize()
    while alive:
        time.sleep(0.1)
        generations += 1
        grid, alive = redraw(grid, generations == 0)
        print("\nGeneration {}".format(generations))
    print("\n\nPopulation lasted {} generations".format(generations))
