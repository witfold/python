def calc_hours(s):
    return sum(map(extract_number, s.split()))


def extract_number(s):
    s = ''.join([i for i in s if i.isnumeric()])
    return int(s) if s != '' else 0


with open('task6.txt', 'r', encoding='utf-8') as f:
    my_dict = dict()
    for line in f.readlines():
        my_dict.update({line.split(":")[0]: calc_hours(line)})

print(my_dict)
