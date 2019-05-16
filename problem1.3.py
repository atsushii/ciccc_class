calculate_result = ""
result = ""
frag = True

print("enter number")
input_number = int(input())

while frag:
    binary_number = input_number % 2
    if input_number // 2 == 0:
        binary_number = input_number % 2
        calculate_result += str(binary_number)
        frag = False
    else:
        input_number = input_number // 2
        calculate_result += str(binary_number)

number_length = len(str(calculate_result))
for i in range(number_length-1, -1, -1):
    result += str(calculate_result)[i]
print(result)
