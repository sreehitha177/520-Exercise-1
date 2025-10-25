# Problem 3: check - Chatgpt Self Planning Solutions
# Task ID: 56
# Description: Write a python function to check if a given number is one less than twice its reverse.

# Solution 1
def check(num):
    rev=int(str(abs(num))[::-1])
    return num==2*rev-1

# Solution 2
def check(num):
    return num+1==2*int(str(num)[::-1])

# Solution 3
def check(num):
    s=str(num)
    r=int(s[::-1])
    return num==(2*r-1)

# Solution 4
def check(num):
    rev=int(''.join(reversed(str(num))))
    return 2*rev-1==num

# Solution 5
def check(num):
    return int(str(num)[::-1])*2-1==num

