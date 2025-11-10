# Problem 4: count_variable - gemini_cot Solution 2
def count_variable(data):
    counts = Counter(data)
    result = []
    for item, count in counts.items():
        result.extend([item] * count)
    return result
