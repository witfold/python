from lesson8.Task4.models.OfficeEquipment import OfficeEquipment


class Scanner(OfficeEquipment):

    def __init__(self, title, price, is_portable=False):
        super().__init__(title, price)
        self.__is_portable = is_portable

    @property
    def is_portable(self):
        return self.__is_portable


