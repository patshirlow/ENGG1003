def myminmax(x):
    low = x[0]
    high = x[0]

    for value in x:
        if value < low:
            low = value
        if value > high:
            high = value
    return low, high

x = [0, 5, 1, -6, 4, 7, -3, -27, 6, -2, 8]
low, high = myminmax(x)
print(low)
print(high)