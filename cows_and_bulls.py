import random


def generate_code():
    for _ in range(4):
        code.append(str(random.randint(0, 10)))


def check_guess(guess):
    cows, bulls = 0, 0
    c = list(code)
    for i in range(4):
        if guess[i] == c[i]:
            cows += 1
            c[i] = "x"
    for i in range(4):
        for j in range(4):
            if guess[i] == c[j]:
                bulls += 1
                c[j] = "y"
    return cows, bulls


code, tries = [], 0
if __name__ == "__main__":
    print("Welcome to the cows and bulls game!")
    generate_code()
    while True:
        guess = input("What's your guess? ")
        tries += 1
        cows, bulls = check_guess(guess)
        if cows == 4:
            print("Congratulations, you cracked the code in {} tries!".format(tries))
            break
        else:
            print("Try {}: You got {} cows and {} bulls".format(tries, cows, bulls))
