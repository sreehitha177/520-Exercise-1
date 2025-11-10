# Problem 6: ap_sum - chatgpt_cot Solution 2
def ap_sum(a, d, n):
    total = 0
    for i in range(n):
        total += a + i * d
    return total
