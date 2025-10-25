# Problem 10: min_sum_path - Chatgpt Self Planning Solutions
# Task ID: 974
# Description: Write a function to find the minimum total path sum in the given triangle.

# Solution 1
def min_sum_path(triangle):
    dp=triangle[-1][:]
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            dp[j]=triangle[i][j]+min(dp[j],dp[j+1])
    return dp[0]

# Solution 2
def min_sum_path(triangle):
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
    return triangle[0][0]

# Solution 3
def min_sum_path(triangle):
    dp=[row[:] for row in triangle]
    for i in range(len(dp)-2,-1,-1):
        dp[i]=[dp[i][j]+min(dp[i+1][j],dp[i+1][j+1]) for j in range(len(dp[i]))]
    return dp[0][0]

# Solution 4
def min_sum_path(triangle):
    res=triangle[-1][:]
    for i in reversed(range(len(triangle)-1)):
        res=[triangle[i][j]+min(res[j],res[j+1]) for j in range(len(triangle[i]))]
    return res[0]

# Solution 5
def min_sum_path(triangle):
    import copy
    dp=copy.deepcopy(triangle)
    for i in range(len(dp)-2,-1,-1):
        for j in range(len(dp[i])):
            dp[i][j]+=min(dp[i+1][j],dp[i+1][j+1])
    return dp[0][0]

