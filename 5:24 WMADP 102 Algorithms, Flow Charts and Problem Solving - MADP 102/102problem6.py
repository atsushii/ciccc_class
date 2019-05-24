# @param number the input number
def prime_check(number):
    # Function Header: prime_check(number)
    # List of parameter: number
    # return: output value
    number = int(number)
    if number <= 1:
        return 'enter number bigger than 1'

    while True:
        number += 1
        if not number % 2 == 0:
            return number


def main():
    # problem 6
    print(prime_check(input('enter number')))


main()
