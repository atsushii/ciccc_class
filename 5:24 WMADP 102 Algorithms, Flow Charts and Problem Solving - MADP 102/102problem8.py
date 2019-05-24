# @param number the input number
def reverse_number(number):
    # Function Header: reverse_number(number)
    # List of parameter: number
    # return: output reverse number
    reverse_number = ""
    number = is_invalid(number)

    for i in range(len(number) - 1, -1, -1):
        reverse_number += number[i]

    return reverse_number

# @param number the input number
def is_invalid(number):
    # Function: is_invalid(number)
    # List of parameter: number
    # return: output valid number
    while True:
        if '.' in number or int(number) % 10 == 0:
            number = input('enter valid number')
        else:
            return number

def main():
    # prpblem8
    print(reverse_number(input('enter number')))

main()
