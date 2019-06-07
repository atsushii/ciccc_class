class MyCustomList:
    def __init__(self):
        self.my_list = []

    def add_item(self):
        while True:
            number = input('enter integer number')
            if number == '':
                break
            if number not in self.my_list:
                self.my_list.append(int(number))

    def calculate_sum(self):
        num_sum = 0
        for i in self.my_list:
            num_sum += i
        return num_sum

    def calculate_max(self):
        max_number = 0
        for i in self.my_list:
            if max_number < i:
                max_number = i
        return max_number

    def print_list(self):
        return self.my_list


class TestClass:

    @staticmethod
    def test_my_custom_list():
        my_custom_list = MyCustomList()
        my_custom_list.add_item()
        print(my_custom_list.calculate_sum())
        print(my_custom_list.calculate_max())
        print(my_custom_list.print_list())
