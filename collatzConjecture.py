# Implimentation of Collatz conjecture
count = 0
while not count:
    c0 = int(input("Please enter a non-negative, non-zero integer: "))
    while c0 > 1:
        if (c0%2 == 0):
            c0 //= 2
        else:
            c0 = (3 * c0 + 1)
        print(c0)
        count += 1
    if count > 0:
        print("steps =",count, sep=" ")
