height = int(input("Diamond height? "))
j = 1
for i in range(height // 2, 0, -1):
    print(" " * i + "*" * j + "\n")
    j += 2
j = height
for i in range(0, height // 2 + 1):
    print(" " * i + "*" * j + "\n")
    j -= 2

