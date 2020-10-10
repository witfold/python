import random

numbers = [random.randint(1, 30) for i in range(10)]

print(f'Default list: {numbers}')
print([numbers[i + 1] for i in range(len(numbers) - 1) if numbers[i] < numbers[i + 1]])
