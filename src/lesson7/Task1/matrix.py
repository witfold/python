class Matrix:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__items = []

    def add_row(self, items):
        if len(self.items) != self.__rows:
            if self.__columns == len(items):
                self.__items.append(items)
            else:
                print('Cannot add row: Different column size')
        else:
            print('Cannot add row: Rows already filled')

    def __is_new_items_with_same_column_size(self, items):
        return len({len(_) for _ in self.items + items}) == 1

    @property
    def items(self):
        return self.__items

    def __str__(self):
        return '\n'.join([str(elem) for elem in self.__items])

    def __eq__(self, other):
        return len(self.items) == len(other.items) \
            and len({len(_) for _ in self.items + other.items}) == 1

    def __add__(self, other):
        if self != other:
            print('Different matrix size')
            return self
        else:
            result = Matrix(self.__rows, self.__columns)
            for i, item in enumerate(self.items, 0):
                result.add_row([el + other.items[i][j] for j, el in enumerate(item, 0)])
            return result


