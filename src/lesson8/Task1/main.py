class CustomDateException(Exception):
    def __init__(self, msg):
        self.__msg = msg


class Utils:
    @staticmethod
    def get_values_from_string(s):
        return list(map(lambda _: int(_), s.split('-')))


class CustomDate:

    def __init__(self, value):
        if self.validate(value):
            self.__value = value

    @property
    def get_values(self):
        return self.__value

    @classmethod
    def extract_numbers(cls, value):
        print(Utils.get_values_from_string(value) if cls.validate(value)
              else 'Cannot extract numbers from invalid value')

    @staticmethod
    def validate(value):
        try:
            values = Utils.get_values_from_string(value)
            if values[0] not in range(1, 32):
                raise CustomDateException('Wrong day, please try again, available values 1-31')
            if values[1] not in range(1, 13):
                raise CustomDateException('Wrong month, please try again, available values 1-12')
            if values[2] not in range(1980, 2021):
                raise CustomDateException('Wrong year, please try again, available values 1980-2020')
            return True
        except (ValueError, CustomDateException) as e:
            print(f'{e}')
            return False


