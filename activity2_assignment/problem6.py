def row_columns(create_list):
    """
    return max sum of number of cell

    parameter
    --------------
    create_list :
        create twe dimension list

    return
    --------------
    cell_tuple : tuple
        cell (row, column)
    """

    cell_tuple = ()
    max_cell = 0
    for row in range(len(create_list) - 1):

        for columns in range(len(create_list[1]) - 1):

            if (row - 1) < 0 or (row + 1) > (len(create_list) - 1) or (columns - 1) < 0 or (columns + 1) > (len(create_list[1]) - 1):
                continue

            calculate_cell = create_list[row][columns] + create_list[row - 1][columns] + create_list[row + 1][columns] +  create_list[row][columns - 1] + create_list[row][columns + 1]

            if max_cell < calculate_cell:
                max_cell = calculate_cell
                cell_tuple = ('row:', row, 'columns:', columns)
    print(calculate_cell)
    return cell_tuple


def compare_list():
    """
    create compare table

    return
    --------------
    compare_list : list
        use for check empty or not
    """
    compare_list = [[0, 1, 2, 3, 4, 5, 6, 0, 0, 9], [1, 1, 0, 3, 4, 5, 6, 7, 8, 9], [1, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ], [1, 1, 1, 0, 0, 0, 0, 1, 1, 1]]

    return compare_list

def create_list():
    """
    create list

    return
    --------------
    table_list : list
        main list
    """

    table_list = [[0 for i in range(10)] for j in range(8)]
    for row in range(8):
        for column in range(10):
            if compare_list( )[row][column]  == 0:
                table_list[row][column] = 0
            else:
                table_list[row][column] = (row + column) * 3 - 10
    return table_list

def main():
    """
    problem6
    """
    print(row_columns(create_list()))

main()
