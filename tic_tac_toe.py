def horizontals(k):
    print(" ---" * k)

def verticals(k):
    print("|   " * (k+1))

def verticals_and_values(l):
    x = {0:" ", 1:"X", 2:"O"}
    for _ in range(3):
        print("| {} ".format(x[l[_]]), end = "")
    print("|")

def draw_empty():
    size = input("What size game board? ")
    if "x" in size:
        i = int(size.split("x")[0])
        j = int(size.split("x")[1])
    else:
        i = int(size)
        j = i
    for _ in range(j):
        horizontals(i)
        verticals(i)
    horizontals(i)

def draw(l):
    for _ in range(3):
        horizontals(3)
        verticals_and_values(l[_])
    horizontals(3)

def check_horizontals(l):
    x = 0
    for i in range(3):
        t = l[i][0]
        if t is 0: continue
        elif t == l[i][1] and t == l[i][2]:
            x = t
            break
    return x

def check_verticals(l):
    x = 0
    for i in range(3):
        t = l[0][i]
        if t is 0: continue
        elif t == l[1][i] and t == l[2][i]:
            x = t
            break
    return x

def check_diagonals(l):
    t = l[0][0]
    if t != 0 and t == l[1][1] and t == l[2][2]: return t
    t = l[0][2]
    if t != 0 and t == l[1][1] and t == l[2][0]: return t
    return 0

def check_board(l):
    w = check_horizontals(l)
    if w == 0: w = check_verticals(l)
    if w == 0: w = check_diagonals(l)
    return w

def print_winner(w):
    if w != 0: print("Winner is Player {}!".format(w))
    else:print("No winner.")

def get_move(pieces,l):
    if pieces % 2 == 0: turn = 1
    else: turn = 2
    while True:
        move = input("Enter your move Player {}, in the form <row,column>: ".format(turn)).strip()
        if "," not in move: print("Invalid move, try again")
        else:
            x = int(move.split(",")[0])
            y = int(move.split(",")[1])
            if x < 1 or x > 3 or y < 1 or y > 3: print("Invalid coordinates, try again")
            else:
                m = l[x-1][y-1]
                if m is not 0: print("Player {} already marked that space, try again".format(m))
                else:
                    l[x-1][y-1] = turn
                    break


def play():
    l = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    winner, pieces = 0, 0
    while winner == 0 and pieces < 9:
        print("State of board:")
        draw(l)
        get_move(pieces,l)
        pieces += 1
        if pieces >= 5: winner = check_board(l)
    draw(l)
    print_winner(winner)
    return winner

if __name__ == "__main__":
    again = "y"
    scores = [0, 0]

    while again == "y":
        scores[play()-1] +=1
        again = input("Play again? (y/n) ")
    print("Scores: Player 1: {}, Player 2: {}".format(scores[0], scores[1]))