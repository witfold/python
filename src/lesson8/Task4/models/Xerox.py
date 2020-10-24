from lesson8.Task4.models.OfficeEquipment import OfficeEquipment


class Xerox(OfficeEquipment):

    def __init__(self, title, price, is_wifi=False):
        super().__init__(title, price)
        self.__is_wifi = is_wifi

    @property
    def is_wifi(self):
        return self.__is_wifi
