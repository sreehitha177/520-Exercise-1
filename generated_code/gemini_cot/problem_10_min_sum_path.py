# Problem 10: min_sum_path - Gemini Cot Solutions
# Task ID: 974
# Description: Write a function to find the minimum total path sum in the given triangle.

# Solution 1
def min_sum_path(triangle):
    if not triangle:
        return 0
    for row_index in range(len(triangle) - 2, -1, -1):
        current_row = triangle[row_index]
        next_row = triangle[row_index + 1]
        for col_index in range(len(current_row)):
            min_next = min(next_row[col_index], next_row[col_index + 1])
            current_row[col_index] += min_next
    return triangle[0][0]

# Solution 2
def min_sum_path(triangle):
    if not triangle:
        return 0
    num_rows = len(triangle)
    dp = list(triangle[num_rows - 1])
    for i in range(num_rows - 2, -1, -1):
        current_row = triangle[i]
        new_dp = [0] * len(current_row)
        for j in range(len(current_row)):
            new_dp[j] = current_row[j] + min(dp[j], dp[j+1])
        dp = new_dp
    return dp[0]

# Solution 3
def min_sum_path(triangle):
    if not triangle:
        return 0
    memo = {}
    def solve(r, c):
        if r == len(triangle) - 1:
            return triangle[r][c]
        if (r, c) in memo:
            return memo[(r, c)]
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
    dp_row = list(triangle[-1])
    for i in range(len(triangle) - 2, -1, -1):
        current_row = triangle[i]
        for j in range(len(current_row)):
            dp_row[j] = current_row[j] + min(dp_row[j], dp_row[j+1])
    return dp_row[0]

# Solution 5
def min_sum_path(triangle):
    if not triangle:
        return 0
    for row_idx in range(len(triangle) - 2, -1, -1):
        for col_idx in range(len(triangle[row_idx])):
            current_val = triangle[row_idx][col_idx]
            triangle[row_idx][col_idx] = current_val + min(
                triangle[row_idx + 1][col_idx],
                triangle[row_idx + 1][col_idx + 1]
            )
    return triangle[0][0]