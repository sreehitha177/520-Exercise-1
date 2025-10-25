# Problem 5: find_tuples - Chatgpt Self Planning Solutions
# Task ID: 75
# Description: Write a function to find tuples which have all elements divisible by k from the given list of tuples.

# Solution 1
def find_tuples(lst,k):
    return [t for t in lst if all(x%k==0 for x in t)]

# Solution 2
def find_tuples(lst,k):
    res=[]
    for t in lst:
        if all(x%k==0 for x in t): res.append(t)
    return res

# Solution 3
def find_tuples(lst,k):
    return list(filter(lambda t: all(x%k==0 for x in t), lst))

# Solution 4
def find_tuples(lst,k):
    out=[]
    for t in lst:
        div=True
        for e in t:
            if e%k!=0: div=False; break
        if div: out.append(t)
    return out

# Solution 5
def find_tuples(lst,k):
    return [t for t in lst if min(t)%k==0]

