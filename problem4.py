# problem 4

# initialize
reverse_string = ""
check_input_string = ""
input_string = str(input())
input_string_length = len(input_string)

# print reverse input string
for i in range(0, input_string_length):
    reverse_string += input_string[input_string_length - 1 - i]
print(reverse_string)

reverse_string_length = len(reverse_string)

# fix input string from reverse
for i in range(0, reverse_string_length):
    check_input_string += reverse_string[reverse_string_length - 1 - i]

# Check the input string and the its reverse is the same
if input_string == check_input_string:
    print('This is correct')
