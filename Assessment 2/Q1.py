import integration as integ
import numpy as np

# a i)
def f(x):
    return 7 + 14 * x ** 6

def trapezoidal_vs_polynomial():
    exact = 9
    approx = integ.trapezoidal(f, 0, 1, 100)
    return exact - approx
print(trapezoidal_vs_polynomial())

def simpson_vs_polynomial():
    exact = 9
    approx = integ.simpson(f, 0, 1, 100)
    return exact - approx
print(simpson_vs_polynomial())

# a ii)
def f_2(x):
    return 2 / 1 + x ** 2
def trapezoidal_vs_hyperbola():
    exact = np.pi / 2
    approx = integ.trapezoidal(f_2, 0, 1, 100)
    return exact - approx
print(trapezoidal_vs_hyperbola())

def simpson_vs_hyperbola():
    exact = np.pi / 2
    approx = integ.simpson(f, 0, 1, 100)
    return exact - approx
print(simpson_vs_hyperbola())

# a iii)
def f_3(x):
    return np.sqrt(x - x ** 2)
def trapezoidal_vs_sqrt():
    exact = np.pi
    approx =  (3 * np.sqrt(3) / 4) + 24 * integ.trapezoidal(f_3, 0, 1/4, 100)
    return exact - approx
print(trapezoidal_vs_sqrt())
def simpson_vs_sqrt():
    exact = np.pi / 2
    approx = (3 * np.sqrt(3) / 4) + 24 * integ.simpson(f_3, 0, 1/4, 100)
    return exact - approx
print(simpson_vs_sqrt())

# b i)
def numerical_std_normal(a, b):
    def g(x):
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-x ** 2 / 2)
    result = integ.simpson(g, a, b, 1000)
    return result

# b ii)
def random_std_normal(a, b):
    N = 10 ** 6
    np.random.seed(1)
    X = np.random.normal(0, 1, N)
    count = 0
    for i in range(N):
        if (X[i] >= a) and (X[i] <= b):
            count += 1
    result = count / N
    return result

