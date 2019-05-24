# @param input_string input message
def call_function(input_string):
    # Function Header: call_function(input_string)
    # List of parameter: input_string
    # return output result 1 or 0 with message
    result_reverse_string = reverse_string(input_string)
    return check_string(result_reverse_string, input_string)

# @param input_string input message
def reverse_string(input_string):
    # Function : reverse_string(input_string)
    # List of parameter: input_string
    # return output reverse string message
    reverse_string = ""
    input_string_length = len(input_string)
    for i in range(0, input_string_length):
        reverse_string += input_string[input_string_length - 1 - i]
    return reverse_string

# @param reverse_string reverse string message
# @param input_string string message
def check_string(reverse_string, input_string):
    # Function : check_string(reverse_string, input_string):
    # List of parameter: reverse_string, input_string
    # return output result
    if reverse_string == input_string:
        return 1
    else:
        return "0: It considers case-sensitivity which means (" +  reverse_string + " and " + input_string + " are not the same)"


def main():
    # problem14
    print(call_function(input('enter message')))

main()
