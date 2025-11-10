# Problem 10: min_sum_path - chatgpt_self_planning Solution 2
def min_sum_path(triangle):
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
    return triangle[0][0]
