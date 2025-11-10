# Problem 9: largest_pos - gemini_cot Solution 2
def largest_pos(lst):
    max_val = None
    found_positive = False
    for x in lst:
        if isinstance(x, (int, float)) and x > 0:
            if not found_positive or x > max_val:
                max_val = x
                found_positive = True
    return max_val
