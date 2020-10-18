elements = list(input('Write down the list items with spaces in between: ').split(' '))
print(f'Default list: {elements}')

for i in range(0, len(elements) - 1, 2):
    elements[i], elements[i + 1] = elements[i + 1], elements[i]
    # tmp = elements[i]
    # elements[i] = elements[i+1]
    # elements[i+1] = tmp

print(f'Processed list {elements}')
