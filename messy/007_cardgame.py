# rank: 2,3,4,5,6,7,8,9,T,J,Q,K,A
# suit: c,d,h,s (clubs,diamonds,hearts,spades)
rank = str(input("Enter card rank: "))
suit = str(input("Enter card suit: "))
if rank == "A" and suit == "s":
    print("First Prize")    # ace of spades
elif rank == "A":   # any other ace
    print("Second Prize")
else:
    print("No Prize")