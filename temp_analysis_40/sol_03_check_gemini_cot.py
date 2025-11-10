# Problem 3: check - gemini_cot Solution 2
def check(n):
    if not isinstance(n, int) or n < 0:
        return False
    n_str = str(n)
    rev_str = n_str[::-1]
    try:
        n_rev = int(rev_str)
    except ValueError:
        return False
    return n == (2 * n_rev) - 1
