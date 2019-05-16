print("enter twe number")
first_number = int(input())
second_number = int(input())

for i in range(first_number + 1, second_number):
    if i % 15 == 0:
        print("(A and B not included", i)

for i in range(first_number, second_number):
    if i % 6 == 0 or i % 7 == 0:
        print(" (A included by B not included", i)

for i in range(first_number, second_number + 1):
    if not i % 3 == 0:
        print("A and B both included", i)
