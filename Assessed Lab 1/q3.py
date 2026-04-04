total = 30   #total cost of item in dollars
is_member = False    #True if the customer is a member, otherwise false

if total < 0:
    print("Invalid total")
elif is_member and total >= 30:
    print("Shipping: $0")
elif total >= 50:
    print("Shipping: $0")
else:
    print("Shipping: $5")