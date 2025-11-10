# Problem 7: extract_elements - Gemini Cot Solutions
# Task ID: 898
# Description: Write a function to extract specified number of elements from a given list, which follow each other continuously.


# Solution 1
def extract_elements(lst, n):
    if n <= 0 or not lst or n > len(lst):
        return []
    result = []
    for i in range(len(lst) - n + 1):
        sub_list = lst[i : i + n]
        result.append(sub_list)
    return result

# Solution 2
def extract_elements(lst, n):
    if n <= 0 or n > len(lst):
        return []
    return [lst[i:i + n] for i in range(len(lst) - n + 1)]

# Solution 3
def extract_elements(lst, n):
    if n <= 0 or n > len(lst):
        return []
    return [
        lst[i:i+n]
        for i in range(len(lst))
        if i + n <= len(lst)
    ]

# Solution 4
def extract_elements(lst, n):
    if n <= 0 or n > len(lst):
        return []
    slices = (lst[i:] for i in range(n))
    return [list(tup) for tup in zip(*slices)]

# Solution 5
def extract_elements(lst, n):
    if n <= 0 or n > len(lst):
        return []
    indices = range(len(lst) - n + 1)
    return [lst[i:i + n] for i in indices]