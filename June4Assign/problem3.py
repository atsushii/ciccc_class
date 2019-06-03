def check_list(repeate_number_list):
    """
    return repeated number

    parameter
    --------------
    repeate_number_list : list
        there are exactly 2 in the list except one number that is repeated only once.

    return
    -------------
    repeate_number_list : list
        one number that is repeated only once.
    """

    repeate_count = 0
    for i in range(len(repeate_number_list)):
        for n in repeate_number_list:
            if repeate_number_list[i] == n:
                repeate_count += 1

        if repeate_count == 1:
            return repeate_number_list[i]

        repeate_count = 0

def main():
    """
    problem3
    create list from input number
    """

    repeate_number_list = []

    while True:
        input_num = input('enter integer list')
        if input_num == '':
            break
        repeate_number_list.append(int(input_num))

    print(check_list(repeate_number_list))

main()
