# a, b, c
import numpy as np
import rootfinding as rf

def f(x):
	return np.exp(x) - 3*x

xLO = 0
xHI = 1

x, iters = rf.bisection(f, xLO, xHI)
print(f"Bisection solution: x = {x:.6f}")
print(f"Check: {f(x):.5f}")
print(f"Iteration count: {iters}")

x0 = 0
x1 = 1
x, iters = rf.secant(f, x0, x1)
print(f"Secant solution: x = {x:.6f}")
print(f"Check: {f(x):.5f}")
print(f"Iteration count: {iters}")

