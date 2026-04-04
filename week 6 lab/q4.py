import numpy as np
x = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
angle = np.sin(x)
for a in angle:
    print(f"{a:.3f}")