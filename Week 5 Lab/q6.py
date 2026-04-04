import numpy as np

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def erf(x, n):
    total = 0
    for i in range(0, n):
        sign = (-1) ** i
        numerator = x ** (2 * i + 1)
        denominator = (2 * i + 1) * factorial(i)
        term = sign * numerator / denominator
        total += term
    return (2 / (np.pi) ** 0.5) * total
x = 0.5
n = 5
result = erf(x, n)
print(result)