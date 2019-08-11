s = input("New game? enter 'n' to quit... ")
possible = ["r", "p", "s"]
while s != "n":
    s1, s2 = "", ""
    while s1 not in possible:
        s1 = input("Enter player 1 move: ")
    while s2 not in possible:
        s2 = input("Enter player 2 move: ")
    if s1 == s2:
        print("No winner")
    elif s1 == "r" and s2 == "p":
        print("Congrats Player 2")
    elif s1 == "p" and s2 == "s":
        print("Congrats Player 2")
    elif s1 == "s" and s2 == "r":
        print("Congrats Player 2")
    else:
        print("Congrats Player 1")
    s = input("New game? enter 'n' to quit... ")

