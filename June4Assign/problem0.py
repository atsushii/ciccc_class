def check_list(repeate_number_list):
    """
    check most repeated number

    parameter
    --------------
    repeate_number_list : list
        it has repeated number
    """

    keep_number_count = 0
    repeate_count = 0
    most_repeated_number = 0
    for i in range(len(repeate_number_list)):
        for n in repeate_number_list:
            if repeate_number_list[i] == n:
                repeate_count += 1

        if repeate_count > keep_number_count:
            keep_number_count = repeate_count
            most_repeated_number = repeate_number_list[i]

        repeate_count = 0

    return most_repeated_number

def main():
    """
    problem0
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
