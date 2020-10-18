class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    def _get_income(self):
        return self.__income


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, {'wage': wage, 'bonus': bonus})

    def get_full_name(self):
        print(f'({self.name} {self.surname}, Position - {self.position})')

    def get_total_income(self):
        print(f'Total income: {sum(self._get_income().values())}')


posit = Position('aaa', 'bbb', 'director', 100, 100)
posit.get_total_income()
posit.get_full_name()

posit = Position('zzz', 'xxx', 'manager', 50, 49)
posit.get_total_income()
posit.get_full_name()
