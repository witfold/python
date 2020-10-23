import math


class OrganicCell:

    def __init__(self, num_of_cells):
        self.__num_of_cells = num_of_cells

    @property
    def get_number_of_cells(self):
        return self.__num_of_cells

    def __add__(self, other):
        return self.get_number_of_cells + other.get_number_of_cells

    def __sub__(self, other):
        res = self.get_number_of_cells - other.get_number_of_cells
        if res > 0:
            return res
        else:
            print('Cannot subtract cells, was returned first cell')
            return self.get_number_of_cells

    def __mul__(self, other):
        return self.get_number_of_cells * other.get_number_of_cells

    def __truediv__(self, other):
        return int(self.get_number_of_cells / other.get_number_of_cells)

    def __get_cell_symbol(self):
        return '*'

    def beauty_print(self, count_of_items_per_line):
        count_of_groups = math.ceil(self.get_number_of_cells / count_of_items_per_line)
        return '\n'.join([self.__get_cell_symbol() * count_of_items_per_line if _ != count_of_groups - 1
                          else self.__get_cell_symbol() * (self.get_number_of_cells - (_ * count_of_items_per_line))
                          for _ in range(0, count_of_groups)])

