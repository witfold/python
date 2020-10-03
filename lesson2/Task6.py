items = []

specification = {
    'name': '',
    'price': 0,
    'count': 0,
    'dimension': ''
}

result = {}

while True:
    print(f'Existing items: {items}')
    command = input('Type \'exit\' for stop or \'add\' for continue typing: ')

    if command == 'exit':
        break
    elif command == 'add':
        for key in specification.keys():
            specification[key] = input(f'Enter {key} value: ')
            if key in result:
                result.get(key).add(specification[key])
            else:
                result[key] = {specification[key]}
        items.append((len(items) + 1, specification.copy()))
    else:
        print('Unknown command, please use \'add\' or \'exit\'')

print(f'Unique values: \n {result}')
