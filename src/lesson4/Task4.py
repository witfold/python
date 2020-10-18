from random import randint

numbers = [randint(1, 10) for _ in range(10)]

print(f'Default list: {numbers}')
print(f'Result: {[el for el in numbers if numbers.count(el) == 1]}')
