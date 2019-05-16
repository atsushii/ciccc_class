frag = True
count = 1
max = 0
min = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet)
while frag:
    print("enter numbers")
    input_number = input()

    for i in range(0, alphabet_length):
        if  alphabet[i] in input_number.lower():
            frag = False
            print("max", max,"\n" "min", min)
            print("distance", "%d" % (abs(max) - abs(min)))
    # for文で複数回見てるからprintを繰り返してる count 使う

    if count == 1 and frag == True:
        max = int(input_number)
        min = int(input_number)

    if max < int(input_number) and frag == True:
        max = int(input_number)
    elif min > int(input_number) and frag == True:
        min = int(input_number)

    count += 1
