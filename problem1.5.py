x = 2
frag = True
while frag:
    F1 = 2 ** x
    F2 = x ** 5

    if F1 > F2:
        T = x
        frag = False
    else:
        x += 1

print(T)
