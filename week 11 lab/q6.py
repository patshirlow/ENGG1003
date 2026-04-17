import numpy as np
import matplotlib.pyplot as plt
import rootfinding as rf

# a
x = np.linspace(-1, 5, 1001)
def f(x):
    return np.exp(x) - 3 * (x ** 2)

plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.title('exp(x) - 3(x**2)')
plt.show()

# x values are between [-1, 0], [0, 2], [3, 4]

# b
xLO, xHI = -1, 0
x, iters = rf.bisection(f, xLO, xHI)
print(f'{x:.5f}')

xLO, xHI = 0, 2
x, iters = rf.bisection(f, xLO, xHI)
print(f'{x:.5f}')

xLO, xHI = 3, 4
x, iters = rf.bisection(f, xLO, xHI)
print(f'{x:.5f}')



