frag = True
reverse_number = ""
print("enter number")

while frag:
    input_num = int(input())
    if input_num % 10 == 0 or input_num % -10 == 0:
        print("enter number")
        input_num = int(input())
    else:
        number_length = len(str(input_num))
        for i in range(number_length-1, -1, -1):
            reverse_number += str(input_num)[i]
        print(reverse_number)
        frag = False
