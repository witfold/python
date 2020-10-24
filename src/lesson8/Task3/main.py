class ConvertException(Exception):
    def __init__(self, msg):
        self.__msg = msg


def custom_check_is_numeric(s):
    try:
        float(s)
        return True
    except Exception:
        raise ConvertException('Please write only numbers')


items = []
while command := input('Write number or \'stop\' to exit: '):
    if command.lower() == 'stop':
        break
    try:
        if custom_check_is_numeric(command):
            items.append(float(command))
    except Exception as e:
        print(f'{e}')

print(items)
