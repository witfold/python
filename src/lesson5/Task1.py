with open('task1.txt', 'w') as f:
    while text := input('>!'):
        f.write(text + '\n')
