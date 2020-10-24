from lesson8.Task4.models.OfficeEquipment import OfficeEquipment


class Printer(OfficeEquipment):

    def __init__(self, title, price, is_color=False):
        super().__init__(title, price)
        self.__is_color = is_color

    @property
    def is_color(self):
        return self.__is_color
