# @param number the twe input numbers
def calculator_result(a, b):
    # Function Header: calculator_result(a, b)
    # List of parameter: a, b
    # return: output value
    x = 2
    while True
        F1 = a ** x
        F2 = x ** b

        if F1 > F2:
            T = x
            return a, b, T
        else:
            x += 1

def main():
    # problem12
    a = int(input('enter number'))
    b = int(input('enter number'))
    print(calculator_result(a, b))

main()
