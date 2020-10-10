from itertools import islice, count, cycle
from sys import argv

if len(argv) != 2:
    print('Please give an argument with integer value')
else:
    try:
        number = int(argv[1])

        elements = [i for i in islice(count(number), 8)]
        print(elements)

        iterator = cycle(elements)
        print([next(iterator) for i in range(1, len(elements) * 2 + 1)])
    except ValueError:
        print('Param should be with int type')
