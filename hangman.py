import random


def read_file_into_list():
    with open("in/sowpods.txt", "r") as f:
        l = f.readlines()
    return l


def choose_word(l):
    return random.choice(l).strip()


def ask_for_guess(word, l):
    hit = False
    win = False
    while True:
        c = input("Enter your guess: ").upper()
        if c in l:
            print("Letter is already in there!")
        else:
            break

    if c not in word:
        print("Letter not in word!")
    else:
        hit =  True
        for i in range(len(word)):
            if c == word[i]:
                l[i] = c
        if "-" not in l:
            win = True
    return win, hit


def guess_word(word, limit=6):
    print(word)
    l = list("-" * len(word))
    tries = 0

    while limit > 0:
        print("".join(l))
        win, hit = ask_for_guess(word, l)
        if not win:
            if not hit:
                limit -= 1
            graphic(limit)
            tries += 1
        else:
            break
    if win:
        print(
            "Congratulations, it took you {} tries to guess the word correctly!".format(
                tries
            )
        )
    else:
        print("Game over, better luck next time")


def graphic(limit):
    print("       ***")
    print("       ***")
    print("       ***")
    if limit == 4:
        print("     *******")
        print("     *******")
        print("     *******")
        print("     *******")
    if limit == 3:
        print("    ********")
        print("   * *******")
        print("  *  *******")
        print(" *   *******")
    if limit <= 2:
        print("    *********")
        print("   * ******* *")
        print("  *  *******  *")
        print(" *   *******   *")
    if limit == 1:
        print("      **")
        print("      **")
        print("      **")
        print("      **")
        print("      **")
    if limit == 0:
        print("      ** **")
        print("      ** **")
        print("      ** **")
        print("      ** **")
        print("      ** **")
    print("\n\n\n")

if __name__ == "__main__":
    l = read_file_into_list()
    word = choose_word(l)
    guess_word(word)

