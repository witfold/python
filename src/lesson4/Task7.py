from functools import reduce
from sys import argv


def fact(n):
    if n == 0:
        yield 1
    else:
        for i in range(1, n + 1):
            yield i


if len(argv) != 2:
    print('Please give only one argument with integer value')
else:
    try:
        number = int(argv[1])
        if number < 0:
            print('Argument cannot be less than 0')
        else:
            print(reduce(lambda a, b: a * b, [el for el in fact(number)]))
    except ValueError:
        print('Param should be with int type')



