# Problem 3: check - Gemini Self Planning Solutions
# Task ID: 56
# Description: Write a python function to check if a given number is one less than twice its reverse.

# Solution 1
def check(n):
    if not isinstance(n, int) or n < 0:
        return False
        
    n_str = str(n)
    n_reverse_str = n_str[::-1]
    
    try:
        n_reverse = int(n_reverse_str)
    except ValueError:
        return False
        
    return n == (2 * n_reverse) - 1

# Solution 2
def check(n):
    if not isinstance(n, int) or n < 0:
        return False
        
    original_n = n
    reversed_n = 0
    temp_n = n
    
    while temp_n > 0:
        digit = temp_n % 10
        reversed_n = (reversed_n * 10) + digit
        temp_n //= 10
        
    return original_n == (2 * reversed_n) - 1

# Solution 3
def check(n):
    if not isinstance(n, int) or n < 0:
        return False
        
    n_str = str(n)
    rev_str = "".join(reversed(n_str))
    
    try:
        n_rev = int(rev_str)
    except ValueError:
        return False
        
    return n == (2 * n_rev) - 1

# Solution 4
def check(n):
    if not isinstance(n, int) or n < 0:
        return False
        
    s = str(n)
    s_rev = s[::-1]
    
    try:
        n_rev = int(s_rev)
    except ValueError:
        return False
        
    # The condition n + 1 = 2 * n_rev
    return (n + 1) == (2 * n_rev)

# Solution 5
def check(n):
    if not isinstance(n, int) or n < 0:
        return False
        
    def reverse_recursive(num, reversed_val=0):
        if num == 0:
            return reversed_val
        last_digit = num % 10
        new_reversed = (reversed_val * 10) + last_digit
        return reverse_recursive(num // 10, new_reversed)
        
    n_rev = reverse_recursive(n)
    return n == (2 * n_rev) - 1