# @param input_number number of table line
def call_table(input_number):
    # Function Header: call_table(input_number)
    # List of parameter: input_number
    create_first_line(input_number)
    create_table(input_number)

# @param input_number number of table line
def create_first_line(input_number):
    # Function : create_first_line(input_number)
    # List of parameter: input_number
    print("%5s" % 'x', end = "")
    for i in range(1, input_number + 1):
        print("%5d" % i, end = "")
    print()
    print()

# @param input_number number of table line
def create_table(input_number):
    # Function : create_table(input_number)
    # List of parameter: input_number
    for i in range(1, input_number + 1):
        print("%5d" % i, end = "")
        for n in range(1, input_number + 1):
            print("%5d" % (i * n), end = "")
        print()
        print()
    print()

def main():
    # problem13
    # testcase
    call_table(10)
    call_table(20)
    call_table(5)

main()
