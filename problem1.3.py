# problem 1.3

# initialize
calculate_number = ""
binary_number = ""
flag = True

# input number
print("enter number")
input_number = int(input())

# loop until convert input number to binary number
while flag:
    each_number = input_number % 2
    # check convert to number or not
    if input_number // 2 == 0:
        each_number = input_number % 2
        calculate_number += str(each_number)
        flag = False
    else:
        input_number = input_number // 2
        calculate_number += str(each_number)

number_length = len(str(calculate_number))
# get binary number
for i in range(number_length-1, -1, -1):
    binary_number += str(calculate_number)[i]
print(binary_number)
