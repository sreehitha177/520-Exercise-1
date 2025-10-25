# Problem 1: odd_Num_Sum - Chatgpt Cot Solutions
# Task ID: 549
# Description: Write a python function to find the sum of fifth power of first n odd natural numbers.

# Solution 1
def odd_Num_Sum(n):
    return sum((2 * i - 1) ** 5 for i in range(1, n + 1))

# Solution 2
def odd_Num_Sum(n):
    total = 0
    for i in range(1, n * 2, 2):
        total += i ** 5
    return total

# Solution 3
def odd_Num_Sum(n):
    odds = [x for x in range(1, 2 * n, 2)]
    return sum(pow(x, 5) for x in odds)

# Solution 4
def odd_Num_Sum(n):
    return sum(map(lambda x: (2 * x - 1) ** 5, range(1, n + 1)))

# Solution 5
def odd_Num_Sum(n):
    return sum([(2*i-1)**5 for i in range(1,n+1)])

