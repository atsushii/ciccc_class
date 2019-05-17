for i in range(0, 11):
    for j in range(0, 11):
        n = (i+1) * j
        n2 = (i * j)
        if i == 0 and n == 0:
            n = 'x'
            print('%5s' % n, end="")
        elif i == 0:
            print('%5s' % n, end="")
        elif n2 == 0:
            n2 = i
            print('%5d' % n2, end="")
        else:
            print('%5d' % n2, end="")

    print()
