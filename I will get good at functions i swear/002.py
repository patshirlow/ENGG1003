# 4)
def is_positive(x):
    if x > 0:
        return True
    else:
        return False
print(is_positive(-3))

# 5)
def grade_mark(mark):
    if mark >= 85:
        return "HD"
    elif mark >= 75:
        return "D"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "P"
    else:
        return "F"
print(grade_mark(90))

# 6)
def compare(a, b):
    if a > b:
        return "Greater"
    elif a == b:
        return "Equal"
    else:
        return "Less"
print(compare(95, 90))