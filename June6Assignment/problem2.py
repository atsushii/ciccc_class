class MyCustomList:
    def __init__(self):
        """
        initialize list
        """
        self.my_list = []

    def add_item(self):
        """
        add number to list
        """
        while True:
            number = input('enter integer number')
            if number == '':
                break
            if number not in self.my_list:
                self.my_list.append(int(number))

    def calculate_sum(self):
        """
        calculate sum
        :return: total number
        """
        num_sum = 0
        for i in self.my_list:
            num_sum += i
        return num_sum

    def calculate_max(self):
        """
        calculate max number
        :return: max number
        """
        max_number = 0
        for i in self.my_list:
            if max_number < i:
                max_number = i
        return max_number

    def print_list(self):
        """
        print list
        :return: list
        """
        return self.my_list


class TestClass:

    @staticmethod
    def test_my_custom_list():
        """
        implement class MyCustomList
        """
        my_custom_list = MyCustomList()
        my_custom_list.add_item()
        print(my_custom_list.calculate_sum())
        print(my_custom_list.calculate_max())
        print(my_custom_list.print_list())
