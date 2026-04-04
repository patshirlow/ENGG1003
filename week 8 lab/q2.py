def read_int(prompt):
    try:
        s = input(prompt)
        value = int(s)
    except ValueError:
        print("Invalid integer")
        return None
    else:
        return value
    finally:
        print("done")

print(read_int("Enter whatever bullshit: "))