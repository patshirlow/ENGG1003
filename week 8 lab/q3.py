# a)
from fontTools.misc.arrayTools import pointInRect


def set_temperature(value):
    try:
        temperature = int(value)
        if temperature < -50 or temperature > 60:
            raise ValueError("Temperature out of safe range")
    except ValueError as e:
        print(e)
        return None
    else:
        return temperature

print(set_temperature(10))
print(set_temperature(100))

# b)
def get_temperature():
    while True:
        try:
            s = input("Enter temperature in degrees Celsius: ")
            value = int(s)
            return set_temperature(value)
        except ValueError as e:
            print(e)

print(get_temperature())
