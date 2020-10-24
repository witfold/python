from lesson8.Task4.exceptions.OnlyPositiveNumberException import OnlyPositiveNumberException


class Utils:

    @staticmethod
    def validate_positive_number(s, is_float=False):
        try:
            if (float(s) if is_float else int(s)) <= 0:
                raise OnlyPositiveNumberException()
            return True
        except Exception as e:
            print(f'{e}')
