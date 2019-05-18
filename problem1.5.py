# problem 1.5

# initialize
x = 2
flag = True

# loop until find T
while flag:
    F1 = 2 ** x
    F2 = x ** 5

    # get T
    if F1 > F2:
        T = x
        flag = False
    else:
        x += 1

print(T)
