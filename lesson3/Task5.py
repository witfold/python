def is_exit_symbol(str):
    return str.lower() == 'q'


def sum_numbers(str):
    res = 0
    for s in str.split():
        if not is_exit_symbol(s):
            res += float(s)
    return res


summ = 0
while True:
    print(f'Current sum: {summ}')
    command = input('Type numbers (or symbol \'q\' for stop typing): ')
    summ += sum_numbers(command)
    if command.count('q'):
        break

print(f'Total sum {summ}')
