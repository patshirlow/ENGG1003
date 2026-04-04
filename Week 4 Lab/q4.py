x = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
for n in range(2, 10):
    x[n] = x[n-1] + x[n-2]
print(x)