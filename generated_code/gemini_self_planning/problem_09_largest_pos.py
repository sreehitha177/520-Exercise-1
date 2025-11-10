# Problem 9: largest_pos - Gemini Self Planning Solutions
# Task ID: 517
# Description: Write a python function to find the largest postive number from the given list.

# Solution 1
def largest_pos(lst):
    positive_numbers = [
        x for x in lst 
        if isinstance(x, (int, float)) and x > 0
    ]
    if not positive_numbers:
        return None
    return max(positive_numbers)

# Solution 2
def largest_pos(lst):
    # Generator yields positive numbers
    positive_gen = (
        x for x in lst 
        if isinstance(x, (int, float)) and x > 0
    )
    # max() with default=None handles empty generator case
    return max(positive_gen, default=None)

# Solution 3
def largest_pos(lst):
    max_val = None
    found_positive = False
    for x in lst:
        if isinstance(x, (int, float)) and x > 0:
            if not found_positive or x > max_val:
                max_val = x
                found_positive = True
    return max_val

# Solution 4    
def largest_pos(lst):
    def is_positive_numeric(x):
        return isinstance(x, (int, float)) and x > 0
        
    positive_list = list(filter(is_positive_numeric, lst))
    
    if not positive_list:
        return None
    return max(positive_list)

# Solution 5
def largest_pos(lst):
    positive_numbers = [
        x for x in lst 
        if isinstance(x, (int, float)) and x > 0
    ]
    if not positive_numbers:
        return None
    # Sort the list (O(N log N))
    positive_numbers.sort()
    return positive_numbers[-1]