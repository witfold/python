def custom_sum(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.remove(min(numbers))
    return sum(numbers)


print(custom_sum(1, 2, 0))
