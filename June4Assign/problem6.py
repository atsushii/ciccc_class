def receive_number():
    """
    sum distinct numbers

    return
    --------------------
    total_number : int
        sum of all distinct numbers the userhad entered
    """

    total_number = 0
    numbers_list = []

    while True:

        number = input('enter nuber: ')

        if not number in numbers_list:
            numbers_list.append(number)
            total_number += int(number)
        else:
            print('already entered %s ' % number)
            continue

        if number == '0':
            return total_number

def main():
    """
    problem6

    call function
    """
    print(receive_number())

main()
