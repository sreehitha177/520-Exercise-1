# Problem 1: odd_Num_Sum - gemini_self_planning Solution 2
def odd_Num_Sum(n):
    if n <= 0:
        return 0
    # Generate the list of odd numbers (1, 3, 5, ...) up to the nth term
    odd_powers = [(2 * k - 1) ** 5 for k in range(1, n + 1)]
    return sum(odd_powers)
