# a)
def add(a, b):
    return a + b
print(add(1, 5))

# b)
def sub(a, b):
    return a - b
difference = sub(10, 2)
if difference < 0:
    difference = 0
print(difference)

# c)
def mult(a, b):
    return a * b
product = mult(7, 6)
if product < 0:
    product = 0
print(product)

# d)
def div(a, b):
    if b == 0:
        return 1000
    result = a / b
    if result < 0:
        result = 0
    return result
print(int(div(10, 2)))

# e)
def simple_calc(eq):
    a_str, op, b_str = eq.split(" ")
    a = int(a_str)
    b = int(b_str)
    if b ==0:
        return 1000
    result = 0
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    if result < 0:
        result = 0
    return result
print(simple_calc("1 + 5"))
print(simple_calc("5 - 100"))
print(simple_calc("7 * 6"))







