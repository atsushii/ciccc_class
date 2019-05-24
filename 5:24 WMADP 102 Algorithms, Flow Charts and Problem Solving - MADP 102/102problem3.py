# @param number the input number

def prime_check(number):
    # Function Header: prime_check(number)
    # List of parameter: number
    # return: output value
    number = int(number)
    if number <= 1:
        return False

    if number % 2 == 0:
        return False
    else:
        return True

def main():
    # problem 3
    print(prime_check(input('enter number')))


main()
