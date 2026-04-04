import numpy as np
d = 7 # distance in metres
x = 63 # degrees
h = d * np.tan(x * np.pi/180) # formula for height of tree
print(f"The height of the tree is {h:.3f} metres")