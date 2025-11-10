# Problem 10: min_sum_path - gemini_self_planning Solution 2
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
