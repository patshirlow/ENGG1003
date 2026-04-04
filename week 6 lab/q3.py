import numpy as np
x = 10.0 # Horizontal position
y = 10.0 # Vertical position

angle = np.atan(y/x) # arctan

print((angle/np.pi)*180) # converts to degrees