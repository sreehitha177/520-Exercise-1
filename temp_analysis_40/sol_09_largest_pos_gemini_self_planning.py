# Problem 9: largest_pos - gemini_self_planning Solution 2
def largest_pos(lst):
    # Generator yields positive numbers
    positive_gen = (
        x for x in lst 
        if isinstance(x, (int, float)) and x > 0
    )
    # max() with default=None handles empty generator case
    return max(positive_gen, default=None)
