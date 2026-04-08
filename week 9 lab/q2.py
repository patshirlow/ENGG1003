import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 101)
y = np.exp(x) - 3 * x

plt.plot(x, y)
plt.axis([0, 2, 0, 2])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential')
plt.show()