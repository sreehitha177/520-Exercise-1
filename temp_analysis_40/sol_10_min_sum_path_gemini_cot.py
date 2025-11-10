# Problem 10: min_sum_path - gemini_cot Solution 2
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
