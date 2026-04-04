# a)
def straight_line(c1, c2, x):
    return c1 * x + c2
print(straight_line(1, 0, 1))

# b)
def parabolic_line(c1, c2, c3, x):
    return c1 * x ** 2 + c2 * x + c3
print(parabolic_line(1, 2, 3, 4))

# c)
def cubic_line(c1, c2, c3, c4, x):
    return c1 * x ** 3 + c2 * x ** 2 + c3 * x + c4
print(cubic_line(1, 2, 3, 4, 5))

# d)
def general_polynomial(coeffs, x):
    y = 0
    n = len(coeffs)
    for i in range(n):
        y += coeffs[i] * x ** (n - 1)
    return y
print(general_polynomial([-1, 0.5], 1))