raiting = [7, 5, 3, 3, 2]

while True:
    print(f'Current raiting: {raiting}')
    command = input('Write new number of raiting or type "Exit": ')
    if command.lower() == 'exit':
        break
    new_value = int(command)
    if raiting.count(new_value):
        raiting.reverse()
        i = raiting.index(new_value)
        raiting.reverse()
        new_index = len(raiting) - i
        raiting.insert(new_index, new_value)
    elif new_value > max(raiting):
        raiting.insert(0, new_value)
    elif new_value < min(raiting):
        raiting.insert(len(raiting), new_value)
    else:
        for i, j in enumerate(raiting, 0):
            if new_value > j:
                raiting.insert(i, new_value)
                break
