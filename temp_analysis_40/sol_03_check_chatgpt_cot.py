# Problem 3: check - chatgpt_cot Solution 2
def check(num):
    s = str(num)
    r = int(s[::-1])
    return (num - (2 * r - 1)) == 0
