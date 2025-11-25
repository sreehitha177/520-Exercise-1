def max_difference(pairs):
    if not pairs:                     
        return 0                                   # BUG: should return -1
    max_diff = 0
    for a, b in pairs:
        diff = abs(b - a)
        if diff > max_diff:           
            max_diff = diff
        else:
            pass                      
    if max_diff == 0:                 
        return 0
    return max_diff



