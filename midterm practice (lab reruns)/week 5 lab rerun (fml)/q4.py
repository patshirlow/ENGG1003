x = [4, 6, 12, 2]

def myminmax(x):
    min = x[0]
    max = x[0]
    for num in x:
        if num < min:
            min = num
        if num > max:
            max = num
    return min, max
print(myminmax(x))
