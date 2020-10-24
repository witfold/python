from functools import reduce
from lesson8.Task7.CustomComplex import CustomComplex


def input_number(label, is_imaginary_part=False):
    while True:
        try:
            res = float(input(f'{label}: '))
            if is_imaginary_part and res == 0:
                print('Part of complex number cannot be 0 (e.g. 2i, 3i...)')
            else:
                return res
        except Exception as e:
            print(e)


items = [CustomComplex(2, 3), CustomComplex(3, -1)]
while True:
    print(f'Existing Items: {[str(_) for _ in items]}')
    print('Put \'1\' for add item')
    print('Put \'2\' for sum items')
    print('Put \'3\' for multiply items')
    print('Put \'4\' for clear items')
    print('Put \'0\' for exit\n')
    cmd = input('Type command: ')
    if cmd == '0':
        break
    elif cmd == '1':
        print('Please set X and Y: (complex number +/- X +/- Yi')
        while True:
            items.append(CustomComplex(input_number('X: '), input_number('Y: ', True)))
            break
    elif cmd == '2':
        print(sum(items))
    elif cmd == '3':
        print(reduce(lambda a, b: a * b, items))
    elif cmd == '4':
        items.clear()
