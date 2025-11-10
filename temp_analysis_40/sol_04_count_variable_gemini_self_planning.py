# Problem 4: count_variable - gemini_self_planning Solution 2
from collections import defaultdict
def count_variable(data):
    # Use a dictionary to count frequencies
    counts = defaultdict(int)
    for item in data:
        counts[item] += 1
        
    result = []
    # Use the original list to determine the order of unique elements
    seen = set()
    for item in data:
        if item not in seen:
            count = counts[item]
            result.extend([item] * count)
            seen.add(item)
    return result
