# Problem 5: find_tuples - Chatgpt Cot Solutions
# Task ID: 75
# Description: Write a function to find tuples which have all elements divisible by k from the given list of tuples.

# Solution 1
def find_tuples(lst, k):
    return [t for t in lst if all(x % k == 0 for x in t)]

# Solution 2
def find_tuples(lst, k):
    res = []
    for tup in lst:
        if all(elem % k == 0 for elem in tup):
            res.append(tup)
    return res

# Solution 3
def find_tuples(lst, k):
    return list(filter(lambda t: all(i % k == 0 for i in t), lst))

# Solution 4
def find_tuples(lst, k):
    out = []
    for t in lst:
        divisible = True
        for e in t:
            if e % k != 0:
                divisible = False
                break
        if divisible:
            out.append(t)
    return out

# Solution 5
def find_tuples(lst, k):
    return [t for t in lst if min(t)%k==0]

