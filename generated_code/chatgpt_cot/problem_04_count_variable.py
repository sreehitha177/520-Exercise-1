# Problem 4: count_variable - Chatgpt Cot Solutions
# Task ID: 810
# Description: Write a function to iterate over elements repeating each as many times as its count.

# Solution 1
from collections import Counter
def count_variable(lst):
    c = Counter(lst)
    res = []
    for k, v in c.items():
        res.extend([k] * v)
    return res

# Solution 2
def count_variable(lst):
    return [x for x in lst for _ in range(lst.count(x))]

# Solution 3
def count_variable(lst):
    d = {}
    for item in lst:
        d[item] = d.get(item, 0) + 1
    out = []
    for k, v in d.items():
        out += [k] * v
    return out

# Solution 4
def count_variable(lst):
    return sum(([x] * lst.count(x) for x in dict.fromkeys(lst)), [])

# Solution 5
def count_variable(lst):
    from collections import Counter
    res = []
    for k,v in Counter(lst).items():
        res+=[k]*v
    return res

