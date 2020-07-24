def add_float(a,b, tolerance = 1e-8):
    ##We make a value error incase tolerance is negative
    if not tolerance >= 0:
        raise ValueError ("Value should be non negative")
    return abs(a-b) < tolerance