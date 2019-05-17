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

    if count == 1 and frag == True:
        max = int(input_number)
        min = int(input_number)

    if frag == True and max < int(input_number):
        max = int(input_number)
    elif frag == True and min > int(input_number):
        min = int(input_number)

    count += 1
print("max", max,"\n" "min", min)
print("distance", "%d" % (abs(max) - abs(min)))
