temperature = 85
pressure = 110

# the system is considered safe is the temperature is below 80 degrees celsius
# and if the pressure is below 120 kPa

if temperature < 80 and pressure < 120:
    print("SAFE")
else:
    print("UNSAFE")