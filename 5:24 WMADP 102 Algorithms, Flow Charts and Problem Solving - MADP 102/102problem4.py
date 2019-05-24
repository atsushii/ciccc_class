# @param number the input number
def add_number(number):
    # Function Header: add_number(number):
    # List of parameter: number
    # return: output result sum number, mean and standard_deviation
    total = 0
    n = 0
    deviation = 0
    deviation_list = []

    while number != 0:
        total += number
        n += 1
        mean = total / n
        deviation_list.append(number)
        number = int(input('enter number'))

    for deviation_number in deviation_list:
         deviation += (deviation_number - mean) ** 2

    variance = deviation / n
    standard_deviation = variance ** 0.5

    return total, mean, standard_deviation

def main():
    # problem4

    print(add_number(int(input('enter number'))))

main()
