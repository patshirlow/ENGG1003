import numpy as np

def areapoly(n, s = 1):
    area = 1/4 * n * (s ** 2) * (1/np.tan(np.pi/n))
    return area

n= 5
print(areapoly(n))
print(areapoly(n, s=2))

