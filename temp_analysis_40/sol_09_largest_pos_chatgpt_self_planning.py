# Problem 9: largest_pos - chatgpt_self_planning Solution 2
def largest_pos(lst):
    res=None
    for x in lst:
        if x>0 and (res is None or x>res): res=x
    return res
