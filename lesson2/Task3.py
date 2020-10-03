seasons = {
    'winter': (12, 1, 2),
    'spring': (3, 4, 5),
    'summer': (6, 7, 8),
    'autumn': (9, 10, 11)
}

while True:
    month = int(input('Please enter the month number: '))
    if month not in range(1, 12):
        print('Wrong number, please try again, available values 1-12')
    else:
        for key, value in seasons.items():
            if month in value:
                print(key)
        break
