# @param first_number the first input number
# @param second_number the second input number
# @param operator input operator
# return result which is sum of first_number and second_number or -, % or *
def calculator(first_number, second_number, operator):
    # Function Header: calculator(first_number, second_number, operator)
    # List of parameter: first_number, second_number and operator
    # return: output value

    if int(first_number) >= 0 and int(second_number) == 0 and operator == '/':
        return "the operation is not possible because one number if zero (this is only for division operator)."

    if operator == '+':
        return int(first_number) + int(second_number)
    elif(operator == '-'):
        return int(first_number) - int(second_number)
    elif(operator == '*'):
        return int(first_number) * int(second_number)
    else:
        return int(first_number) / int(second_number)

def main():
    # problem1.1
    # testcase
    print(calculator(1, 1, '+'))
    print(calculator(10, 0, '+'))

    print(calculator(1, 1, '-'))
    print(calculator(10, 0, '-'))

    print(calculator(1, 1, '*'))
    print(calculator(10, 0, '*'))

    print(calculator(1, 1, '/'))
    print(calculator(10, 0, '/'))


main()
