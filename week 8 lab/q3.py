# a)
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


