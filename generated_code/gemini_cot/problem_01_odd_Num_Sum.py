# Problem 1: odd_Num_Sum - Gemini Cot Solutions
# Task ID: 549
# Description: Write a python function to find the sum of fifth power of first n odd natural numbers.


# Solution 1
def odd_Num_Sum(n):
    if not isinstance(n, int) or n < 1:
        return 0
    total_sum = 0
    for k in range(1, n + 1):
        odd_num = 2 * k - 1
        total_sum += odd_num ** 5
    return total_sum

# Solution 2
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

# Solution 3
def odd_Num_Sum(n):
    if n <= 0:
        return 0
    return sum([(2 * k - 1) ** 5 for k in range(1, n + 1)])

# Solution 4
def odd_Num_Sum(n):
    if n <= 0:
        return 0
    return sum((pow(2 * k - 1, 5) for k in range(1, n + 1)))

# Solution 5
from functools import reduce
def odd_Num_Sum(n):
    if n <= 0:
        return 0
    odd_powers = (pow(2 * k - 1, 5) for k in range(1, n + 1))
    return reduce(lambda acc, x: acc + x, odd_powers, 0)

