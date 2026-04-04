# a)
def straight_line(c1, c2, x):
    y = c1 * x + c2
    return y
print(straight_line(1, 0, 1))

# b)
def parabolic_line(c1, c2, c3, x):
    y = c1 * (x ** 2) + c2 * x + c3
    return y
print(parabolic_line(1, 2, 3, 4))

# c)
def cubic_line(c1, c2, c3, c4, x):
    y = c1 * (x ** 3) + c2 * (x ** 2) + c3 * x + c4
    return y
print(cubic_line(1, 2, 3, 4, 5))

# d)
def general_polynomial(coeffs, x):
    n = len(coeffs)
    y = 0
    for i in range(n):
        y += coeffs[i] * (x ** (n - 1 - i))
    return y
print(general_polynomial([-1, 0.5,], 1))
