# Problem 6: ap_sum - Gemini Cot Solutions
# Task ID: 335
# Description: Write a function to find the sum of arithmetic progression.


# Solution 1
def ap_sum(a, n, d):
    if not isinstance(n, int) or n <= 0:
        return 0
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
    terms_generator = (a + i * d for i in range(n))
    return sum(terms_generator)

# Solution 5
def ap_sum(a, n, d):
    if n <= 0:
        return 0
    numerator = n * (2 * a + (n - 1) * d)
    sum_n = numerator / 2.0
    return int(sum_n) if sum_n == int(sum_n) else sum_n