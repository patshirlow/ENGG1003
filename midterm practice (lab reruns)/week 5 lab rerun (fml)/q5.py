def minpos(x):
    mp = 0
    idx = 0

    for i in range(len(x)):
        if x[i] > 0:
            if mp == 0 or x[i] < mp:
                mp = x[i]
                idx = i
    if mp == 0:
        print("List has no positive values")

    return mp, idx
x = [1.624, -0.611, -1.072, 0.865, -2.301, 1.744, -0.761, 0.319, -0.249]

mp, idx = minpos(x)
print(x)
print(mp)
print(idx)