class Bed:
    bed_type = 'king_size_bed'

    def __init__(self, pillow, blanket, sheet, second_pillow, mattress):
        self.pillow = pillow
        self.blanket = blanket
        self.sheet = sheet
        self.second_pillow = second_pillow
        self.mattress = mattress

    def set_summer_pillow(self, water_pillow):
        self.pillow = water_pillow

    def get_pillow(self):
        return self.pillow

    def print_pillow(self):
        print(self.pillow)

    def print_blanket(self):
        print(self.blanket)


class Table:
    table_type = 'big_table'

    def __init__(self, laptop, money, food, book, stand_light):
        self.laptop = laptop
        self.money = money
        self.food = food
        self.book = book
        self.stand_light = stand_light

    def set_food(self, snacks):
        self.food = snacks

    def get_pillow(self):
        return self.food

    def print_money(self):
        print(self.money)

    def print_book(self):
        print(self.book)


class Shelf:
    shelf_type = 'big_shelf'

    def __init__(self, clothe, bag_pack, shoes, stuff, hanger):
        self.clothe = clothe
        self.bag_pack = bag_pack
        self.shoes = shoes
        self.stuff = stuff
        self.hanger = hanger

    def set_clothe(self, clothe):
        self.clothe = clothe

    def get_clothe(self):
        return self.clothe

    def print_stuff(self):
        print(self.stuff)

    def print_shoes(self):
        print(self.shoes)


class School:
    school = 'private_school'

    def __init__(self, table, member, time, teacher, assignment):
        self.table = table
        self.member = member
        self.time = time
        self.teacher = teacher
        self.assignment = assignment

    def set_assignment(self, assignment):
        self.assignment = assignment

    def get_assignment(self):
        return self.assignment

    def print_member(self):
        print(self.member)

    def print_time(self):
        print(self.time)


class House:
    house = 'share_house'

    def __init__(self, house_mate, price, location, room, size):
        self.house_mate = house_mate
        self.price = price
        self.location = location
        self.room = room
        self.size = size

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def print_location(self):
        print(self.location)

    def print_size(self):
        print(self.size)


def main():
    bed = Bed('small_pillow', 'small_blanket', 'white_sheet', 'big_pillow', 'hot_mattress')
    bed.set_summer_pillow('water_pillow')
    bed.get_pillow()

    table = Table('mac', '1000$', 'fruit', 'textbook', 'small_light')
    table.set_food('snacks')
    table.get_book()

    shelf = Shelf('shirt', 'nixon', 'nike', 'stuff', '5')
    shelf.set_clothe('white_shirt')
    shelf.get_clothe()

    school = School('5', '20', '6', 'Ali', 'python')
    school.set_assignment('None')
    school.get_assignment()

    house = House('5', '650', 'Renfrew', '5', 'big')
    house.set_price('100')
    house.get_price()


main()
