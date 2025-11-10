# Problem 5: find_tuples - chatgpt_cot Solution 2
def find_tuples(lst, k):
    res = []
    for tup in lst:
        if all(elem % k == 0 for elem in tup):
            res.append(tup)
    return res
