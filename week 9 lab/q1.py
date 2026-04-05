import numpy as np
import matplotlib.pyplot as plt

v0 = 5
g = 9.81
t = np.linspace(0, 1, 1001)
y = v0 * t - 0.5 * g * t ** 2

plt.plot(t, y, 'g--') # plot y versus t
plt.ylabel('ball height, y (m)')
plt.xlabel('time, t (s)')
plt.grid(True)
plt.title('ball height over time [0,1] seconds')
plt.legend(['y = v0 * t - 0.5 * g * t ** 2'])
plt.axis([0, 1, 0, 1.4])
plt.show()