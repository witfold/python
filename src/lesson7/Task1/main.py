from lesson7.Task1.matrix import Matrix

m1 = Matrix(3, 2)
m1.add_row([1, 2])
m1.add_row([3, 4])
m1.add_row([5, 6])
print(m1)

m2 = Matrix(3, 2)
m2.add_row([10, 20])
m2.add_row([30, 40])
m2.add_row([50, 60])
print(m2)

m3 = Matrix(3, 2)
m3.add_row([100, 200])
m3.add_row([300, 400])
m3.add_row([500, 600])


print(f'\n{m1+m2+m3}')
