def exponentiation(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    return res if y >= 0 else round(1 / res, 6)


base_of_degree = float(input('Type base of degree: '))
exponent = int(input('Type exponent: '))
print(exponentiation(base_of_degree, exponent))

