def mirror_list(twe_dimension_list):
    """
    return mirror array from arg list

    parameter
    --------------
    twe_dimension_list : list
        twe dimension list

    return
    --------------
    (first_tuple,) + (second_tuple,) : tuple
        mirror array
    """

    first_tuple = ()
    second_tuple = ()

    for i in range(len(twe_dimension_list[1])):
        first_tuple += (twe_dimension_list[1][i],)

    for i in range(len(twe_dimension_list[0])):
        second_tuple += (twe_dimension_list[0][i],)

    return (first_tuple,) + (second_tuple,)
def main():
    """
    problem7
    """
    # testcase
    twe_dimension_list = [[10,20,30], [40,50,60]]

    print(mirror_list(twe_dimension_list))

main()
