# Tested 2016-06-08 21:47

def end_other(a, b):
    # CodingBat solution is easier, but this exercises string slicing.
    return True if (a.lower() == b[len(b)-len(a):].lower() or b.lower() == a[len(a)-len(b):].lower()) else False
