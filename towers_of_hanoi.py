import os
import time

hanoi = [[], [], [], []]
move_list = []
moves = 0


def towers(n, src, dest, temp):
    if n == 1:
        move(src, dest)
    else:
        towers(n - 1, src, temp, dest)
        move(src, dest)
        towers(n - 1, temp, dest, src)


def move(src, dest):
    s, d = src - 1, dest - 1
    global moves
    moves += 1
    time.sleep(0.1)
    move_list.append("Move disk from tower {} to tower {}\n".format(src, dest))
    hanoi[d][hanoi[3][d]] = hanoi[s][hanoi[3][s] - 1]
    hanoi[3][d] += 1
    hanoi[s][hanoi[3][s] - 1] = -1
    hanoi[3][s] -= 1
    showState()


def showState():
    _ = os.system("cls")
    for i in range(3):
        print("Tower {}: ".format(i + 1), end="")
        for j in range(hanoi[3][i]):
            print("{} ".format(hanoi[i][j]), end="")
        print("")
    time.sleep(0.5)


def init(n):
    hanoi[0] = [_ for _ in range(n, 0, -1)]
    hanoi[1] = [-1 for _ in range(n)]
    hanoi[2] = [-1 for _ in range(n)]
    hanoi[3] = [n, 0, 0]
    move_list.append("Towers of Hanoi with {} disks...\n\n".format(n))
    showState()


if __name__ == "__main__":
    n = int(input("How many disks? "))
    init(n)
    towers(n, 1, 3, 2)
    s = "\nCompleted after {} moves! ".format(moves)
    move_list.append(s + "\n")
    os.makedirs("out", exist_ok=True)
    with open("out/towers_{}disks.txt".format(n), "w") as f:
        f.writelines(move_list)
    print(s)
