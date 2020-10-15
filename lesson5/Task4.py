ru_dict = {
    1: 'Один',
    2: 'Два',
    3: 'Три',
    4: 'Четыре'
}

with open('task4_en.txt', 'r', encoding='utf-8') as en_f:
    with open('task4_ru.txt', 'w', encoding='utf-8') as ru_f:
        ru_f.writelines(
            [line.replace(line.split(' - ')[0], ru_dict[int(line.split(' - ')[1])]) for line in en_f.readlines()])
