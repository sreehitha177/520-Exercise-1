# Problem 7: extract_elements - Chatgpt Cot Solutions
# Task ID: 898
# Description: Write a function to extract specified number of elements from a given list, which follow each other continuously.

# Solution 1
def extract_elements(lst, n):
    return [lst[i:i+n] for i in range(len(lst) - n + 1)]

# Solution 2
def extract_elements(lst, n):
    res = []
    for i in range(0, len(lst) - n + 1):
        res.append(lst[i:i+n])
    return res

# Solution 3
def extract_elements(lst, n):
    return list(map(lambda i: lst[i:i+n], range(len(lst) - n + 1)))

# Solution 4
def extract_elements(lst, n):
    i, out = 0, []
    while i + n <= len(lst):
        out.append(lst[i:i+n])
        i += 1
    return out

# Solution 5
def extract_elements(lst, n):
    return [lst[x:x+n] for x in range(len(lst)-n+1)]

