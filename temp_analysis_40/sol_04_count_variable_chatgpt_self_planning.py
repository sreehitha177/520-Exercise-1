# Problem 4: count_variable - chatgpt_self_planning Solution 2
def count_variable(lst):
    return [x for x in lst for _ in range(lst.count(x))]
