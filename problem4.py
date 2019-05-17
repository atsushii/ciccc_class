input_character = str(input())

input_character_length = len(input_character)
result = ""
check_input_character = ""
for i in range(0, input_character_length):
    a = input_character[input_character_length - 1 - i]
    result += a
print(result)

result_length = len(result)

for i in range(0, result_length):
    a = result[result_length - 1 - i]
    check_input_character += a

if input_character == check_input_character:
    print('This is correct')
