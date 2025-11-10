# Problem 4: count_variable - chatgpt_cot Solution 2
def count_variable(lst):
    d = {}
    for item in lst:
        d[item] = d.get(item, 0) + 1
    out = []
    for k, v in d.items():
        out += [k] * v
    return out
