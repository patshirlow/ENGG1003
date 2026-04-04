temp = float(input("Enter the temperature: "))
if temp < 0:
    print("Freezing")
elif 0 <= temp <= 15:
    print("Cold")
elif 16 <= temp <= 25:
    print("Mild")
elif 26 <= temp <= 35:
    print("Warm")
elif temp == 100:
    print("Boiling point!")
else:
    print("Hot")

if -5 <= temp <= 5:
    print("Take care on the roads")