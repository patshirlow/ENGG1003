import numpy as np
import matplotlib.pyplot as plt
import rootfinding as rf
# a

x = np.linspace(-2, 4, 1001)
def f(x):
    return 3 * x + np.sin(x) - np.exp(x)

plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.title('3x + sin(x) - exp(x)')
plt.show()

# b, c
xLO = 0
xHI = 1

x, iters = rf.bisection(f, xLO, xHI)
print(f"{x:.5f}")

xLO, xHI = 1, 2
x, iters = rf.bisection(f, xLO, xHI)
print(f"{x:.5f}")
