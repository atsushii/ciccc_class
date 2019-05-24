def add_number(number):
    total = 0
    n = 0
    deviation = 0
    deviation_total = 0
    variance = 0

    while number != 0:
        total += number
        n += 1
        mean = total / n
        number_list = number
        number = int(input('enter number'))

    deviation = number - mean
    deviation_total += (deviation **2)
    standard_deviation = variance ** 0.5
    return total, mean, standard_deviation

def main():

    print(add_number(int(input('enter number'))))



main()
