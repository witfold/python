class CustomComplex:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __radd__(self, other):
        return self + other if other else self

    def __add__(self, other):
        return CustomComplex(self.x + other.x, self.y + other.y)

    def __rmul__(self, other):
        return self * other

    def __mul__(self, other):
        return CustomComplex(self.x * other.x - self.y * other.y, self.x * other.y + other.x * self.y)

    def __str__(self):
        return f'{self.x}' \
               f'{"-" if self.__y < 0 else "+"}' \
               f'{abs(self.y) if abs(self.y) != 1 else ""}' \
               f'i'

