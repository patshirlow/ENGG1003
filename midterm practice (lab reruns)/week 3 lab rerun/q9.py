is_staff = False
is_student = True
fees_paid = False

if is_staff:
    print("Access Granted")
elif is_student and fees_paid:
    print("Access Granted")
else:
    print("Access Denied")