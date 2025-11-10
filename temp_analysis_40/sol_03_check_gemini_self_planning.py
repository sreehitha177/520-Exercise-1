# Problem 3: check - gemini_self_planning Solution 2
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
