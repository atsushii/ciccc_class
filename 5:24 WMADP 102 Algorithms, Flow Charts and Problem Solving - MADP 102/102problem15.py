# @param input_statement input statement
def call_function(input_statement):
    # Function Header: call_function(input_statement)
    # List of parameter: input_statement
    # return output result message statement is valid or not
    if check_operations(input_statement):
        return check_alphabet(input_statement)
    return "input statement is invalid"

# @param input_statement input statement
def check_operations(input_statement):
    # Function : check_operations(input_statement)
    # List of parameter: input_statement
    # return output statement includs operations or not
    count = 0
    operations_array = ("+", "-", "/", "%", "(", ")")
    for i in operations_array:
        if i in input_statement:
            count += 1
    if count > 0:
        return True
    return False

# @param input_statement input statement
def check_alphabet(input_statement):
    # Function : check_alphabet(input_statement)
    # List of parameter: input_statement
    # return output result message statement is valid or not
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(alphabet)):
        for n in range(len(input_statement)):
            if alphabet[i] == input_statement[n]:
                return "input statement is valid"

    return "input statement is invalid"

def main():
    # problem15
    print(call_function(input('enter statement')))

main()
