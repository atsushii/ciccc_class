# problem3

# create frame
for i in range(0, 11):
    # create each line
    for j in range(0, 11):
        # frame number
        n = (i+1) * j
        n2 = (i * j)
        # put first word
        if i == 0 and n == 0:
            n = 'x'
            print('%5s' % n, end="")
            # create line frame
        elif i == 0:
            print('%5s' % n, end="")
            # create row frame
        elif n2 == 0:
            n2 = i
            print('%5d' % n2, end="")
        else:
            # create each table
            print('%5d' % n2, end="")

    print()
