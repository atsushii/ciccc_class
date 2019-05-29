def bubble_sort(sort_list):
    """
    implement bubble sort

    parameter
    --------------
    sort_list : list
         list

    return
    --------------
    sort_list : list
        sort list
    """

    for i in range(len(sort_list)):
        for n in range(len(sort_list) - 1, i, -1):
            if sort_list[n] < sort_list[n - 1]:
                sort_list[n], sort_list[n - 1] = sort_list[n - 1], sort_list[n]
    return sort_list


def main():
    """
    priblem8
    """
    sort_list = [543, 121, 5324, 2, 1, 6]
    print(bubble_sort(sort_list))

main()
