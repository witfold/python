from random import randint

with open('task5.txt', 'w+') as f:
    print(*[randint(1, 10) for _ in range(20)], sep=' ', file=f)
    f.seek(0)
    print(sum(map(lambda s: int(s), f.read().split())))
