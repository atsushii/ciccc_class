def check_list(repeate_number_list):
    """
    return distinct list

    parameter
    --------------
    repeate_number_list : list
        it has repeated number

    return
    --------------
    distinct_list : list
        only include distinct number

    """
    repeate_count = 0
    distinct_list = []
    for i in range(len(repeate_number_list)):
        for n in repeate_number_list:
            if repeate_number_list[i] == n:
                repeate_count += 1

        if repeate_count <= 1 and not repeate_number_list[i] in distinct_list:
            distinct_list.append(repeate_number_list[i])

        repeate_count = 0

    return distinct_list

def main():
    """
    problem2
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
