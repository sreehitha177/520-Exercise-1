# Problem 7: extract_elements - chatgpt_cot Solution 2
def extract_elements(lst, n):
    res = []
    for i in range(0, len(lst) - n + 1):
        res.append(lst[i:i+n])
    return res
