number = int(input('Enter the number: '))

total_sum = number
count = 0
next_number = str(number)

while count < 2:
    next_number = next_number + str(number)
    total_sum += int(next_number)
    count += 1

print(f'Total sum = {total_sum}')
