# a)
# div_by_zero.py
def div(a, b):
    return a / b

result = div(10, 5)
print(result)

# b)
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "no"

print(safe_divide(10, 0))
print(safe_divide(10, 5))

# c)
def safe_divide2(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "no"
    except TypeError:
        return "are you being fr?"

print(safe_divide2("Hello", 5))
print(safe_divide2(12, 3))
