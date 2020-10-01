number = int(input('Enter the number: '))

biggest_digit = 0

while number > 0:
    tmp_digit = number % 10
    if tmp_digit > biggest_digit:
        biggest_digit = tmp_digit
    number //= 10

print(f'Biggest digit: {biggest_digit}')
