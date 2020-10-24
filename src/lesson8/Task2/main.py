class CustomDivisionByZero(Exception):
    def __init__(self, msg):
        self.__msg = msg


def get_user_number(label, is_divider=False):
    while True:
        try:
            num = float(input(f'{label}: '))
            if is_divider and num == 0:
                raise CustomDivisionByZero('Custom division by zero called')
            return num
        except Exception as e:
            print(e)


print('Please write A and B for calculate \"A / B\"')
a = get_user_number('A')
b = get_user_number('B', True)
print(a / b)



