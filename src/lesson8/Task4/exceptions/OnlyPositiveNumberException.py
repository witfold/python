class OnlyPositiveNumberException(Exception):
    def __init__(self):
        super().__init__("Please write only positive numbers")
