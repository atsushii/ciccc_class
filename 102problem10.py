# @param input_number the 10 base number
def binary_convert(input_number):
    # Function Header: binary_convert(input_number)
    # List of parameter: input_number
    # return: output binary_number
    binary_number = ""
    while input_number > 0:
        division_remainder = input_number % 2
        binary_number = str(division_remainder) + binary_number
        input_number = int(input_number / 2)
    return binary_number


def main():
    # problem 10
    # testcase
    print(binary_convert(10000))
    print(binary_convert(1431))
    print(binary_convert(10024))
    print(binary_convert(-10))

main()
