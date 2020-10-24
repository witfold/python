from abc import ABC
from lesson8.Task4.utils.Utils import Utils


class OfficeEquipment(ABC):

    def __init__(self, title, price):
        self.__title = title
        self.__price = round(float(price), 2) if Utils.validate_positive_number(price, True) else 0

    def __str__(self):
        return f'Name: {self.__title}, Price: {self.__price}'

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if Utils.validate_positive_number(price, True):
            self.__price = round(float(price), 2)
