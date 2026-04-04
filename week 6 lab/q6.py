import numpy as np
t = 6 # time since midnight in hours (6 am)
h = 0.5 * np.cos(np.pi/6.2 * t - 4.25 * np.pi / 6.2) + 1.2
print(f"The water height is {h:.3f}")