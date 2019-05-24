# @param number the input number
def sum_number_digits(number):
    # Function Header: sum_number_digits(number):
    # List of parameter: number
    # return: output value

    sum_number = 0

    if int(number) <= 0:
        return 'only positive number'
    for i in range(0, len(number)):
        sum_number += int(number[i])
    return sum_number


def main():
    # problem5

    print(sum_number_digits(input('enter number')))


main()
