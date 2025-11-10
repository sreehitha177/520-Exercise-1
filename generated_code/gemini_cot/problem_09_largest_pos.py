# Problem 9: largest_pos - Gemini Cot Solutions
# Task ID: 517
# Description: Write a python function to find the largest postive number from the given list.


# Solution 1
def largest_pos(lst):
    positive_numbers = [x for x in lst if isinstance(x, (int, float)) and x > 0]
    if not positive_numbers:
        return None
    return max(positive_numbers)

# Solution 2
def largest_pos(lst):
    max_val = None
    found_positive = False
    for x in lst:
        if isinstance(x, (int, float)) and x > 0:
            if not found_positive or x > max_val:
                max_val = x
                found_positive = True
    return max_val

# Solution 3
def largest_pos(lst):
    try:
        positive_numbers = [x for x in lst if isinstance(x, (int, float)) and x > 0]
        return max(positive_numbers)
    except ValueError:
        return None

# Solution 4
def largest_pos(lst):
    positive_numbers = [x for x in lst if isinstance(x, (int, float)) and x > 0]
    return max(positive_numbers, default=None)

# Solution 5
def largest_pos(lst):
    positive_numbers = [x for x in lst if isinstance(x, (int, float)) and x > 0]
    if not positive_numbers:
        return None
    positive_numbers.sort()
    return positive_numbers[-1]