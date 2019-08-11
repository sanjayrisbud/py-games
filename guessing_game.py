import random


def game():
    i, j, k = 0, 0, random.randint(1, 100)
    while j != k:
        j = int(input("Enter your guess: "))
        i += 1
        if j < k:
            print("Higher!")
        elif j > k:
            print("Lower!")
    return i


s = ""
while s != "n":
    print("Took {} guesses".format(game()))
    s = input("Play again? ")
