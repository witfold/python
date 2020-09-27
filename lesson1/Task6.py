km_first_day = float(input('Number of Km\'s in first day: '))
goal = float(input('Your goal (Km): '))

current_result = km_first_day
goal_day = 1

while current_result < goal:
    current_result += current_result / 10
    goal_day += 1

print(f'Result will be done on {goal_day} day')
