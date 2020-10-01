seconds = int(input('Enter the number of seconds: '))

hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds %= 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')
