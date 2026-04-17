import numpy as np
import integration as integ

# a
def f(x):
    return (2 * x + 3) ** 2
T = integ.trapezoidal(f, -1, 2)
S = integ.simpson(f, -1, 2)
print(f"{T:.3f}")
print(f"{S:.3f}")