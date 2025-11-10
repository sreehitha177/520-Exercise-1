# Problem 7: extract_elements - gemini_self_planning Solution 2
def extract_elements(lst, n):
    if n <= 0 or n > len(lst):
        return []
    result = []
    max_start_index = len(lst) - n
    for i in range(max_start_index + 1):
        sub_list = lst[i : i + n]
        result.append(sub_list)
    return result
