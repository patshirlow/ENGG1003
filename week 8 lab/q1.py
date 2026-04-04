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
        print("no")
        return None

print(safe_divide(10, 0))
print(safe_divide(10, 5))
