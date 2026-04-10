import numpy as np # imports
# a, b, c
def factNum(n):
    total = 1
    try:
        for i in range(1, n + 1):
            total *= i
        if n < 0:
            raise ValueError
        elif n != int(n):
            raise ValueError
        return total
    except TypeError:
        return "Invalid type, input must be an integer"
    except ValueError:
        return "Integer must be positive"

print(factNum(5))

# d, e, f
def sinhNum(x, n):
    total = 0
    try:
        for i in range(1, n+1):
                total += ((x ** (2*i-1)) / factNum(2 * i - 1))
    except TypeError or ValueError:
        print("Incorrect value given to factNum, try again!")
        return None
    return total
print(sinhNum(2, 5))

# g
x = np.linspace(-5, 5, 101)
print(x)

# h
z = sinhNum(x, 5)
print(z)
