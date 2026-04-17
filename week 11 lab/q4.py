import numpy as np
import rootfinding as rf

# a, b
def f(x):
    return 2 * np.exp(-x) - np.sin(x)

xLO, xHI = 0, 3
x, iters = rf.bisection(f, xLO, xHI)
print(f"{x:.5f}")

xLO, xHI = 2, 5
x, iters = rf.bisection(f, xLO, xHI)
print(f"{x:.5f}")

# c
def f(x):
    return np.exp(x) - x - 2
xLO, xHI = 0, 4
x, iters = rf.bisection(f, xLO, xHI)
print(f"{x:.5f}")

# d
def f(x):
    return np.tan(x) - x - 1
xLO, xHI = 0.5, 1.5
x, iters = rf.bisection(f, xLO, xHI)
print(f"{x:.5f}")