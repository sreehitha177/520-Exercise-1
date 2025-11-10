# Problem 10: min_sum_path - Gemini Self Planning Solutions
# Task ID: 974
# Description: Write a function to find the minimum total path sum in the given triangle.

# Solution 1
def min_sum_path(triangle):
    if not triangle:
        return 0
    
    # Iterate from the second-to-last row up to the top
    for r in range(len(triangle) - 2, -1, -1):
        for c in range(len(triangle[r])):
            # Update the current cell with the minimum of the two paths below it
            triangle[r][c] += min(triangle[r + 1][c], triangle[r + 1][c + 1])
            
    return triangle[0][0]

# Solution 2
def min_sum_path(triangle):
    if not triangle:
        return 0
    
    # Initialize DP array with the last row
    dp_row = list(triangle[-1])
    
    # Iterate upwards from the second-to-last row
    for r in range(len(triangle) - 2, -1, -1):
        current_row = triangle[r]
        for c in range(len(current_row)):
            # Update DP[c] with the minimum path sum passing through T[r][c]
            dp_row[c] = current_row[c] + min(dp_row[c], dp_row[c+1])
            
    return dp_row[0]

# Solution 3
def min_sum_path(triangle):
    if not triangle:
        return 0
        
    memo = {}
    
    def solve(r, c):
        # Base Case: Last row
        if r == len(triangle) - 1:
            return triangle[r][c]
            
        # Check Memoization
        if (r, c) in memo:
            return memo[(r, c)]
            
        # Recursive Step
        current_val = triangle[r][c]
        down_left = solve(r + 1, c)
        down_right = solve(r + 1, c + 1)
        
        result = current_val + min(down_left, down_right)
        memo[(r, c)] = result
        return result

    return solve(0, 0)

# Solution 4
def min_sum_path(triangle):
    if not triangle:
        return 0
        
    n = len(triangle)
    # Initialize DP table (same dimensions as triangle)
    dp = [[0] * (i + 1) for i in range(n)]
    dp[-1] = list(triangle[-1])
    
    # Iterate from the second-to-last row up to the top
    for r in range(n - 2, -1, -1):
        for c in range(len(triangle[r])):
            # The path through T[r][c] is T[r][c] + min(DP[r+1][c], DP[r+1][c+1])
            dp[r][c] = triangle[r][c] + min(dp[r+1][c], dp[r+1][c+1])
            
    return dp[0][0]

# Solution 5
def min_sum_path(triangle):
    if not triangle:
        return 0
    
    # Create a mutable copy to avoid modifying the input triangle
    temp_triangle = [list(row) for row in triangle]

    # Start from the second-to-last row (index N-2)
    for r in range(len(temp_triangle) - 2, -1, -1):
        for c in range(len(temp_triangle[r])):
            temp_triangle[r][c] += min(
                temp_triangle[r + 1][c], 
                temp_triangle[r + 1][c + 1]
            )
            
    return temp_triangle[0][0]