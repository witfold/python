from functools import reduce
import json


def average_for_positive_companies(c_list):
    c_list = [c for c in c_list if c[1] > 0]
    return round(sum([c[1] for c in c_list]) / len(c_list), 2)


with open('task7.txt', 'r', encoding='utf-8') as f:
    companies = dict()
    [companies.update({line.split()[0]:
                           reduce(lambda a, b: float(a) - float(b), line.split()[2:])}) for line in f.readlines()]
    res = [companies, {'average_profit': average_for_positive_companies(companies.items())}]


with open('task7.json', 'w', encoding='utf-8') as f:
    json.dump(res, f)
