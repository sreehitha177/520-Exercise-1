# Problem 6: ap_sum - Gemini Self Planning Solutions
# Task ID: 335
# Description: Write a function to find the sum of arithmetic progression.

# Solution 1
def ap_sum(a, n, d):
    if not isinstance(n, int) or n <= 0:
        return 0
    # Use floating point division for accuracy, then check for integer result
    sum_n = (n / 2.0) * (2 * a + (n - 1) * d)
    return int(sum_n) if sum_n == int(sum_n) else sum_n

# Solution 2
def ap_sum(a, n, d):
    if n <= 0:
        return 0
    last_term = a + (n - 1) * d
    sum_n = (n / 2.0) * (a + last_term)
    return int(sum_n) if sum_n == int(sum_n) else sum_n

# Solution 3
def ap_sum(a, n, d):
    if n <= 0:
        return 0
    current_term = a
    total_sum = 0
    for _ in range(n):
        total_sum += current_term
        current_term += d
    return total_sum

# Solution 4
def ap_sum(a, n, d):
    if n <= 0:
        return 0
    # Generator yields the terms: a, a+d, a+2d, ...
    terms_generator = (a + i * d for i in range(n))
    return sum(terms_generator)

# Solution 5
def ap_sum(a, n, d):
    if n <= 0:
        return 0
    if n == 1:
        return a
    # Sum of n terms is the sum of (n-1) terms plus the nth term
    nth_term = a + (n - 1) * d
    return ap_sum(a, n - 1, d) + nth_term
