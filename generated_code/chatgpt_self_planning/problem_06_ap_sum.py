# Problem 6: ap_sum - Chatgpt Self Planning Solutions
# Task ID: 335
# Description: Write a function to find the sum of arithmetic progression.

# Solution 1
def ap_sum(a,d,n):
    return n*(2*a+(n-1)*d)//2

# Solution 2
def ap_sum(a,d,n):
    total=0
    for i in range(n): total+=a+i*d
    return total

# Solution 3
def ap_sum(a,d,n):
    return sum(a+i*d for i in range(n))

# Solution 4
def ap_sum(a,d,n):
    last=a+(n-1)*d
    return n*(a+last)//2

# Solution 5
def ap_sum(a,d,n):
    return n*((2*a)+(n-1)*d)//2

