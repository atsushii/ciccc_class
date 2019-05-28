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
    (-1, -1) : tuple
        number is non exit in the list

    (index_number, last_index_number) : tuple
        index of the first occurrenceof the number and index of the last occurrenceof the number
    """
    index_count = 0
    match_count = 0
    index_number = 0
    last_index_number = 0

    for i in numbers_list:
        if i == number and match_count == 0:
            index_number = index_count
            match_count += 1
        if i == number and last_index_number < index_count:
            last_index_number = index_count
        index_count += 1
    if index_number == 0:
        return (-1, -1)
    return (index_number, last_index_number)


def main():
    """
    problem3
    call function
    """
    # testcase
    numbers_list = [1,2,4,2,4,1,2]
    number = 2
    print(linear_search_list(numbers_list, number))

    numbers_list = [1,222,4,3,4,1,10]
    number = 2
    print(linear_search_list(numbers_list, number))

main()
