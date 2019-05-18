# problem 1.4

# initialize
flag = True
count = 1
max = 0
min = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet)

# loop user enter alphabet in cluding number
while flag:
    # input number
    print("enter numbers")
    input_number = input()

    # split input number
    for i in range(0, alphabet_length):
        # check alphabet
        if  alphabet[i] in input_number.lower():
            flag = False

    # check number first time
    if count == 1 and flag == True:
        max = int(input_number)
        min = int(input_number)

    # compare input number with previous variables
    if flag == True and max < int(input_number):
        max = int(input_number)
    elif flag == True and min > int(input_number):
        min = int(input_number)

    # check first number or not
    count += 1
print("max", max,"\n" "min", min)
print("distance", "%d" % (abs(max) - abs(min)))
