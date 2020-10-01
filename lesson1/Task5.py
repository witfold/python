proceeds = int(input('Enter the proceeds: '))
costs = int(input('Enter the costs: '))
profit = proceeds - costs

if profit > 0:
    print('Profit')
    profitability = profit / proceeds * 100
    count_of_employees = int(input('Count of employees: '))
    print(f'Profitability - {profitability}, Profit by employee - {profit / count_of_employees}')
elif profit == 0:
    print('No profit, No loss')
else:
    print('Loss')
