# a
import numpy as np
import matplotlib.pyplot as plt
import rootfinding as rf

x = np.linspace(0, 2, 1001)

def f(x):
    return np.exp(x) - 3 * x

plt.plot(x, f(x))
plt.axis([0, 2, -2, 2])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

# b, c
xLO = 1
xHI = 2

x, iters = rf.bisection(f, xLO, xHI)
print(f"Bisection solution: x = {x:.5f}")

x, iters = rf.secant(f, xLO, xHI)
print(f"Secant solution: x = {x:.5f}")


