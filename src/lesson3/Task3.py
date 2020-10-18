def custom_sum(num1, num2, num3):
    # numbers = [num1, num2, num3]
    # numbers.remove(min(numbers))
    # return sum(numbers)
    return sum(sorted([num1, num2, num3])[1:])


print(custom_sum(-1, 2, 0))
