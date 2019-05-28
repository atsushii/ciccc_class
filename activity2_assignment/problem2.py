def linear_search_list(numbers_list, number):
    """
    linear search list

    parameter
    --------------
    numbers_list : integer list
        one dimention list
    number : number to search for

    return
    --------------
    (-1, 0) : tuple
        number is non exit in the list

    (index_number, match_count) : tuple
        index number and count of match number and list
    """

    match_count = 0
    for i in range(len(numbers_list)):
        if numbers_list[i] == number and match_count == 0:
            index_number = i
        if numbers_list[i] == number:
            match_count += 1

    if match_count == 0:
        return (-1, 0)
    return (index_number, match_count)


def main():
    """
    problem2
    call function
    """

    # testcase
    numbers_list = [1,2,4,2,4,1,6]
    number = 2
    print(linear_search_list(numbers_list, number))

    numbers_list = [1,222,4,3,4,1,10]
    number = 2
    print(linear_search_list(numbers_list, number))


main()
