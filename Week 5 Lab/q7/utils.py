def percent_change(old, new):
    if old == 0:
        print("ERROR: old cannot be zero for percent change")
        return 0
    else:
        return((new - old) / abs(old)) * 100