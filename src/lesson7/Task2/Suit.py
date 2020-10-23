from .Clothes import Clothes


class Suit(Clothes):

    def __init__(self, name, h):
        super().__init__(name)
        self.__h = h

    @property
    def h(self):
        return self.__h

    def calculate_fabric_consumption(self):
        return self.h * 2 + 0.3
