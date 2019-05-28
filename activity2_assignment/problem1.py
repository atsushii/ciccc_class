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
    match_count - 1 : int
        match index number

    -1 : int
        number is non exit in the list
    """

    match_count = 0
    for i in numbers_list:
        match_count += 1
        if i == number:
            return match_count - 1
    return -1

def main():
    """
    problem1
    call function
    """

    # testcase
    numbers_list = [1,2,4,2,4,1,6]
    number = 2
    print(linear_search_list(numbers_list, number))

    numbers_list = [1,222,4,3,4,1,10]
    number = 10
    print(linear_search_list(numbers_list, number))

main()
