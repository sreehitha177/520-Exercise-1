# Problem 5: find_tuples - chatgpt_self_planning Solution 2
def find_tuples(lst,k):
    res=[]
    for t in lst:
        if all(x%k==0 for x in t): res.append(t)
    return res
