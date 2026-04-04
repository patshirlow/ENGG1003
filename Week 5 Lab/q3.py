import numpy
import numpy as np
def areapoly(n, s=1):
    return (1/4) * n * (s ** 2) * (1/numpy.tan(numpy.pi / n))
print(areapoly(4))
