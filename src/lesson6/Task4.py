import random


class Car:
    __direction = ['Left', 'Right', 'Forward', 'Backward']

    def __init__(self, speed, color, name):
        self.__speed = speed
        self.__color = color
        self.__name = name

    def go(self):
        print(f'{self.__name} going')

    def stop(self):
        print(f'{self.__name} stopped')

    def turn(self):
        print(f'Turned to: {random.choice(self.__direction)}')

    def show_speed(self):
        print(f'Speed: {self.__speed}')

    def is_police(self):
        print('No')

    def _get_speed(self):
        return self.__speed

    def get_name(self):
        print(f'Car: {self.__name}, Color: {self.__color}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print('Speeding' if self._get_speed() > 60 else self._get_speed())


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print('Speeding' if self._get_speed() > 40 else self._get_speed())


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def is_police(self):
        print('Yes')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


def run_actions(car):
    car.get_name()
    car.go()
    car.turn()
    car.stop()
    car.show_speed()
    car.is_police()
    print()


run_actions(PoliceCar(100, 'red', 'Police'))
run_actions(WorkCar(60, 'white', 'Work'))
run_actions(SportCar(200, 'blue', 'Sport'))
run_actions(TownCar(55, 'yellow', 'Town'))
