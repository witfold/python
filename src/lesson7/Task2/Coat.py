from .Clothes import Clothes


class Coat(Clothes):

    def __init__(self, name, v):
        super().__init__(name)
        self.__v = v

    @property
    def v(self):
        return self.__v

    def calculate_fabric_consumption(self):
        return self.v / 6.5 + 0.5
