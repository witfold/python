import random

numbers = [random.randint(1, 10) for i in range(10)]

print(f'Default list: {numbers}')
print(f'Result: {[el for el in numbers if numbers.count(el) == 1]}')
