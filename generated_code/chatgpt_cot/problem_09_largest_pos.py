# Problem 9: largest_pos - Chatgpt Cot Solutions
# Task ID: 517
# Description: Write a python function to find the largest postive number from the given list.

# Solution 1
def largest_pos(lst):
    pos = [x for x in lst if x > 0]
    return max(pos) if pos else None

# Solution 2
def largest_pos(lst):
    res = None
    for x in lst:
        if x > 0 and (res is None or x > res):
            res = x
    return res

# Solution 3
def largest_pos(lst):
    return max((x for x in lst if x > 0), default=None)

# Solution 4
def largest_pos(lst):
    positives = filter(lambda x: x > 0, lst)
    return max(positives, default=None)

# Solution 5
def largest_pos(lst):
    lst2=[x for x in lst if x>0]
    return max(lst2) if lst2 else None

