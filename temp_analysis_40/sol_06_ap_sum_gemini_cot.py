# Problem 6: ap_sum - gemini_cot Solution 2
def ap_sum(a, n, d):
    if n <= 0:
        return 0
    last_term = a + (n - 1) * d
    sum_n = (n / 2.0) * (a + last_term)
    return int(sum_n) if sum_n == int(sum_n) else sum_n
