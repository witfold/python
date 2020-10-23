from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def calculate_fabric_consumption(self):
        pass

    def calc(self):
        return round(self.calculate_fabric_consumption(), 2)
