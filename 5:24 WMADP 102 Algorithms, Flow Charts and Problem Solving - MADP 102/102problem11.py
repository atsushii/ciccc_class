def calculator_result():
    # Function Header: calculator_result()
    # return: output value
    count = 1
    max = 0
    min = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_length = len(alphabet)

    while True:
        input_number = input('enter number')

        if not is_invalid(alphabet_length, input_number, alphabet):
            print("max", max,"\n" "min", min)
            distance = max - min
            print("distance", abs(distance))
            return

        max, min = first_time_count(input_number, count, max, min)
        max, min = compare_number(max, min, input_number)
        count += 1

# @param alphabet_length length of alphabet
# @param input_number input number
# @param alphabet alphabet for check
def is_invalid(alphabet_length, input_number, ):
    # Function: is_invalid(alphabet_length, input_number, alphabet)
    # List of parameter: alphabet_length, input_number, alphabet
    # return: output check if number is valid or not
    for i in range(0, alphabet_length):
        # check alphabet
        if  alphabet[i] in input_number.lower():
            return False
    return True

# @param input_number input number
# @param count check first time or not
# @param max max number
# @param min min number
def first_time_count(input_number, count, max, min):
    # Function: first_time_count(input_number, count, max, min)
    # List of parameter: input_number, count, max, min
    # return: output max number and min number
    if count == 1:
        return int(input_number), int(input_number)
    return max, min

# @param input_number input number
# @param max max number
# @param min min number
def compare_number(max, min, input_number):
    # Function: compare_number(max, min, input_number)
    # List of parameter: input_number, max, min
    # return: output max number and min number
    if max < int(input_number):
        max = int(input_number)
    elif min > int(input_number):
        min = int(input_number)
    return max, min


def main():
    # problem 11
    calculator_result()

main()
