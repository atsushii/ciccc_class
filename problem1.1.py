# problem 1.1

# initialize variables
flag = True
reverse_number = ""

print("enter number")

# loop until user enter number that divisible by 10
while flag:
    input_num = int(input())

    # check valid number or not
    if input_num % 10 == 0 or input_num % -10 == 0:
        print("enter number")
        input_num = int(input())
    else:
        number_length = len(str(input_num))
        # print reverse number
        for i in range(number_length-1, -1, -1):
            reverse_number += str(input_num)[i]
        print(reverse_number)
        flag = False
