# Problem 1: odd_Num_Sum - gemini_cot Solution 2
def odd_Num_Sum(n):
    if n <= 0:
        return 0
    total_sum = 0
    i = 1
    current_odd = 1
    while i <= n:
        total_sum += current_odd ** 5
        current_odd += 2
        i += 1
    return total_sum
