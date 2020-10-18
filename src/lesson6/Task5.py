class Stationery:
    def __init__(self, title):
        self.__title = title

    def draw(self):
        print(f'Draw with {self.get_title()} ({type(self).__name__})')

    def get_title(self):
        return self.__title


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)


Pen('Pen1').draw()
Pencil('Pencil1').draw()
Handle('Handle1').draw()
