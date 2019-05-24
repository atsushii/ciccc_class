# @param first_number the input number
# @param second_number the input number
def receive_number(first_number, second_number):
    # Function Header: receive_number(first_number, second_number)
    # List of parameter: first_number, second_number
    # return: output mention

    if first_number > second_number or first_number < 0 or second_number < 0:
        return 'try again'
    first_divisible(first_number, second_number)
    second_divisible(first_number, second_number)
    final_divisible(first_number, second_number)


# @param first_number the input number
# @param second_number the input number
def first_divisible(first_number, second_number):
    # Function : first_divisible(first_number, second_number)
    # List of parameter: first_number, second_number
    for i in range(first_number + 1, second_number):
        if i % 15 == 0:
            print("A and B not included", i)

# @param first_number the input number
# @param second_number the input number
def second_divisible(first_number, second_number):
    # Function : second_divisible(first_number, second_number)
    # List of parameter: first_number, second_number
    for i in range(first_number, second_number):
        if i % 6 == 0 or i % 7 == 0:
            print(" A included but B not included", i)

# @param first_number the input number
# @param second_number the input number
def final_divisible(first_number, second_number ):
    # Function : final_divisible(first_number, second_number)
    # List of parameter: first_number, second_number
    for i in range(first_number, second_number + 1):
        if not i % 3 == 0:
            print("A and B both included", i)

def main():
    # problem9

    # testcase
    receive_number(3, 5)
    receive_number(6, 7)
    receive_number(3, 11)
    receive_number(121, 200)
    receive_number(20, 11)
    print(receive_number(20, -11))

main()
