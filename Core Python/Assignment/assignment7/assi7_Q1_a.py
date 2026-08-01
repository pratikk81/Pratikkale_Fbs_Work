

for i in range(1,6):
    for j in range(1, 6 - i + 1):
        print(" ", end=" ")

    print("*", end="")

    if i > 1:
        for j in range(1, 2 * i - 2):
            print(" ", end=" ")
        print("*", end="")

    print()

for i in range(6 - 1, 0, -1):
    for j in range(1, 6 - i + 1):
        print(" ", end=" ")

    print("*", end="")

    if i > 1:
        for j in range(1, 2 * i - 2):
            print(" ", end=" ")
        print("*", end="")

    print()