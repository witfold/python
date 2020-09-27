seconds = int(input('Enter the number of seconds: '))

hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds -= hours * 3600 + minutes * 60

if hours < 10:
    hours = '0' + str(hours)

if minutes < 10:
    minutes = '0' + str(minutes)

if seconds < 10:
    seconds = '0' + str(seconds)

print(f'{hours}:{minutes}:{seconds}')
