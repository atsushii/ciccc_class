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
    new_numbers_list : list
        include integer number except arg number

    """
    new_numbers_list = []
    for i in range(0, len(numbers_list)):
        if numbers_list[i] != number:
            new_numbers_list.append(numbers_list[i])
    return new_numbers_list

def main():
    """
    problem4
    call function
    """
    # testcase
    numbers_list = [1,2,4,2,4,1,2,3]
    number = 4
    print(linear_search_list(numbers_list, number))

    numbers_list = [1,222,4,3,4,1,10]
    number = 222
    print(linear_search_list(numbers_list, number))


main()
