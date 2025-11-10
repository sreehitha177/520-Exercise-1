# Problem 7: extract_elements - gemini_cot Solution 2
def extract_elements(lst, n):
    if n <= 0 or n > len(lst):
        return []
    return [lst[i:i + n] for i in range(len(lst) - n + 1)]
