def custom_div(num1, num2):
    return round(num1 / num2, 2)


def custom_is_numeric(num):
    return num.startswith('-') and num[1:].isdigit() or num.isdigit()


while True:
    first_number = input('Type first number: ')
    if custom_is_numeric(first_number):
        second_number = input('Type second number: ')
        while not (custom_is_numeric(second_number)) or float(second_number) == 0:
            print('Invalid number(cannot contains any symbols or 0), please type again.')
            second_number = input('Type second number: ')
        print(f'Result of div function: {custom_div(float(first_number), float(second_number))}')
        break
    else:
        print('Invalid number, please type again.')
