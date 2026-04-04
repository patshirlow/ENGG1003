# 1)
def fahrenheit_to_celsius(f):
    c = (5/9) * (f - 32)
    return c
print(fahrenheit_to_celsius(105))

# 2)
def projectile_height(v0, t):
    g = 9.81
    return v0 * t - (0.5 * g * (t ** 2))
print(projectile_height(85, 7))

# 3)
def circle_area(r):
    import numpy as np
    return np.pi * r ** 2
print(circle_area(5))