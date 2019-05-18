# problem 1.2

# input twe numbers
print("enter twe numbers")
first_number = int(input())
second_number = int(input())

# print number between A to B not included
for i in range(first_number + 1, second_number):
    # check number A to B
    if i % 15 == 0:
        print("A and B not included", i)

# print number between A to B not included
for i in range(first_number, second_number):
    # check number A to B
    if i % 6 == 0 or i % 7 == 0:
        print(" A included by B not included", i)

# print number between A to B but A and B not included
for i in range(first_number, second_number + 1):
    # check number A to B
    if not i % 3 == 0:
        print("A and B both included", i)
