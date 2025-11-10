# Problem 1: odd_Num_Sum - chatgpt_cot Solution 2
def odd_Num_Sum(n):
    total = 0
    for i in range(1, n * 2, 2):
        total += i ** 5
    return total
