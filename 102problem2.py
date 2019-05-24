# @param number the input number
# @param shape input shape format
def shape_format(number, shape):
    # Function Header: shape_format(number, shape)
    # List of parameter: number, shape
    # return: output value

    if number <= 0:
        return "enter number more than 1"

    if shape == 'SHAPE1':
        return shape1(number)
    elif shape == 'SHAPE2':
        return shape2(number)
    elif shape == 'SHAPE3':
        return shape3(number)
    else:
        return "please enter nnumber and shape"


# @param number the input number
def shape1(number):
    # create shape1
    for i in range(int(number) + 1, 0, -1):
        if i % 2 == 0:
            pass
        else:
            print('*' * i)

# @param number the input number
def shape2(number):
    # create shape2
    for i in range(int(number), 0, -1):
        print('*' * i)

# @param number the input number
def shape3(number):
    # create shape3
    for i in range(0, int(number) + 1):
        print('*' * i)

def main():
    # problem 2
    # teatcase
    shape_format(5, 'SHAPE1')
    shape_format(5, 'SHAPE2')
    shape_format(5, 'SHAPE3')

    # testcase2
    print(shape_format(0, 'SHAPE1'))


main()
