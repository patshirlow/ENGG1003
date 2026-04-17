import numpy as np
import integration as integ

# a
def v(t):
	return 3*t**2*np.exp(t**3)

a = 0
b = 1
trap = integ.trapezoidal(v, a, b)
print(f"Trapezoidal method: {trap:.5f}")

S = integ.simpson(v, a, b)
print(f"Simpsons rule: {S:.5f}")

# b
check = np.exp(1) - 1
print(f"Check: {check:.2f}")

# c
# nevermind that sounds boring
