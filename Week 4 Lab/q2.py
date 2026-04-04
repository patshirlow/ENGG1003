n = 10
total = 0
for i in range(1, n+1):
    total += i**2
print(total)

a = (n * (n + 1) * (2 * n + 1)) / 6
print(int(a))

total_1 = 0
for i in range(1, n+1):
    total_1 += i ** 3
print(total_1)

b = (n ** 2 * ((n + 1) ** 2)) / 4
print(int(b))

total_2 = 0
for i in range(1, 2 * n, 2):
    total_2 += i ** 2
print(total_2)

c = n * (2 * n + 1) * (2 * n - 1) / 3
print(int(c))

