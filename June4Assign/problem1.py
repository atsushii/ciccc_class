def check_list(repeate_number_list):
    """
    check most repeated number

    parameter
    --------------
    repeate_number_list : list
        it has repeated number

    return
    --------------
    count_number_dict : dictionary
        return how many each item is repeated
    """

    repeate_count = 0
    count_number_dict = {}
    for i in range(len(repeate_number_list)):
        for n in repeate_number_list:
            if repeate_number_list[i] == n:
                repeate_count += 1

        if not repeate_number_list[i] in count_number_dict:
            count_number_dict[repeate_number_list[i]] = repeate_count

        repeate_count = 0

    return count_number_dict


def main():
    """
    problem1
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
