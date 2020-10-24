from lesson8.Task4.utils.Utils import Utils


class Store:

    def __init__(self, name):
        self.__name = name
        self.__items = {}

    @property
    def name(self):
        return self.__name

    def __count_by_name(self, name):
        return self.__items[name] if name in self.__items else 0

    def put(self, office_equipment, count):
        if Utils.validate_positive_number(count):
            self.__items[office_equipment.title] = self.__count_by_name(office_equipment.title) + count

    def get(self, office_equipment, count):
        if Utils.validate_positive_number(count):
            count_in_store = self.__count_by_name(office_equipment.title)
            if count_in_store == 0:
                print(f'The {office_equipment.title} not found in store!')
                return
            if count_in_store < count:
                print(f'Maximum you can get {count_in_store} {office_equipment.title}\'s')
                return
            elif count_in_store == count:
                del self.__items[office_equipment.title]
            else:
                self.__items[office_equipment.title] = count_in_store - count

    def __str__(self):
        return str([a for a in self.__items.items()])
