# Values of a b c
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Quadratic Formula
x_1 = (-b - (b ** 2 - (4 * a * c)) ** (1 / 2)) / (2 * a)
x_2 = (-b + (b ** 2 - (4 * a * c)) ** (1 / 2)) / (2 * a)

# roots
print(f"x = {x_1} , {x_2}")
