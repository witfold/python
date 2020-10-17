from functools import reduce


class Road:

    __asphalt = {'thickness': 25, 'weight': 5}

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate(self):
        print(f'Result : {(self.__length * self.__width * reduce(lambda a, b: a * b, self.__asphalt.values())) / 1000} ton')


road = Road(20, 5000)
road.calculate()
