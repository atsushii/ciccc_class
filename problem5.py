flag = True
alphabet_count = 0
count = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
binary_operations = "+-/%*()"

alphabet_length = len(alphabet)
binary_operations_length = len(binary_operations)

print("enter statement")
input_statement = input()
statement_length = len(input_statement)
while flag:

    for i in range(0, alphabet_length):
        for j in range(0, statement_length):
            if alphabet[i] == input_statement[j]:
                keep_variable = True
                if alphabet[i] == input_statement[j] and keep_variable
                    alphabet_count += 1




                for k in range(0, binary_operations_length):
                    if not alphabet[i] == input_statement[j] and binary_operations[k] != input_statement[j]:
                        count += 1

    if count >= 1 or alphabet_count >= 2:
        print("it's wrong statement")
        flag = False
    else:
        print("it's correct statement")
        flag = False
