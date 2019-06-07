class Bed:
    bed_type = 'king_size_bed'

    def __init__(self, pillow, blanket, sheet, second_pillow, mattress):
        """
        initialize instance variables
        :param pillow: initialize pillow
        :param blanket: initialize blanket
        :param sheet: initialize sheet
        :param second_pillow: initialize second_pillow
        :param mattress: initialize mattress
        """
        self.pillow = pillow
        self.blanket = blanket
        self.sheet = sheet
        self.second_pillow = second_pillow
        self.mattress = mattress

    def set_summer_pillow(self, water_pillow):
        """
        set instance variables
        :param water_pillow: set pillow
        :return: instance variable
        """
        self.pillow = water_pillow

    def get_pillow(self):
        """
        getter
        :return: pillow
        """
        return self.pillow

    def print_pillow(self):
        """
        print pillow
        """
        print(self.pillow)

    def print_blanket(self):
        """
        print blanket
        """
        print(self.blanket)


class Table:

    table_type = 'big_table'

    def __init__(self, laptop, money, food, book, stand_light):
        """
        initialize instance variables
        :param laptop: initialize laptop
        :param money: initialize money
        :param food: initialize food
        :param book: initialize book
        :param stand_light: initialize stand_light
        """
        self.laptop = laptop
        self.money = money
        self.food = food
        self.book = book
        self.stand_light = stand_light

    def set_food(self, snacks):
        """
        set instance variable
        :param snacks: set instance variable
        """
        self.food = snacks

    def get_pillow(self):
        """
        get instance variable
        """
        return self.food

    def print_money(self):
        """
        print instance variable
        """
        print(self.money)

    def print_book(self):
        """
        print instance variable
        """
        print(self.book)


class Shelf:
    shelf_type = 'big_shelf'

    def __init__(self, clothe, bag_pack, shoes, stuff, hanger):
        """
        initialize instance variables
        :param clothe: initialize clothe
        :param bag_pack: initialize bag_pack
        :param shoes: initialize shoes
        :param stuff: initialize stuff
        :param hanger: initialize hanger
        """
        self.clothe = clothe
        self.bag_pack = bag_pack
        self.shoes = shoes
        self.stuff = stuff
        self.hanger = hanger

    def set_clothe(self, clothe):
        """
        set initialize variable
        :param clothe: set new variable
        """
        self.clothe = clothe

    def get_clothe(self):
        """
        getter
        """
        return self.clothe

    def print_stuff(self):
        """
        print instance variable
        """
        print(self.stuff)

    def print_shoes(self):
        """
        print instance variable
        """
        print(self.shoes)


class School:
    school = 'private_school'

    def __init__(self, table, member, time, teacher, assignment):
        """
        initialize instance variables
        :param table: initialize table
        :param member: initialize member
        :param time: initialize time
        :param teacher: initialize teacher
        :param assignment: initialize assignment
        """
        self.table = table
        self.member = member
        self.time = time
        self.teacher = teacher
        self.assignment = assignment

    def set_assignment(self, assignment):
        """
        set instance variable
        :param assignment: update new value
        """
        self.assignment = assignment

    def get_assignment(self):
        """
        getter
        """
        return self.assignment

    def print_member(self):
        """
        print instance variable member
        """
        print(self.member)

    def print_time(self):
        """
        print instance variable time
        """
        print(self.time)


class House:
    house = 'share_house'

    def __init__(self, house_mate, price, location, room, size):
        """
        initialize instance variables
        :param house_mate: initialize house_mate
        :param price: initialize price
        :param location: initialize location
        :param room: initialize room
        :param size: initialize size
        """
        self.house_mate = house_mate
        self.price = price
        self.location = location
        self.room = room
        self.size = size

    def set_price(self, price):
        """
        set instance variable price
        :param price: new value
        """
        self.price = price

    def get_price(self):
        """
        getter
        """
        return self.price

    def print_location(self):
        """
        print location
        """
        print(self.location)

    def print_size(self):
        """
        print size
        """
        print(self.size)


def main():
    """
    implement all classes
    """
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
