# Problem 4: count_variable - Gemini Cot Solutions
# Task ID: 810
# Description: Write a function to iterate over elements repeating each as many times as its count.


# Solution 1
def count_variable(data):
    counts = Counter(data)
    final_output = []
    for element, count in counts.items():
        final_output.extend([element] * count)
    return final_output

# Solution 2
def count_variable(data):
    counts = Counter(data)
    result = []
    for item, count in counts.items():
        result.extend([item] * count)
    return result

# Solution 3
def count_variable(data):
    result = []
    seen = set()
    for item in data:
        if item not in seen:
            count = data.count(item)
            result.extend([item] * count)
            seen.add(item)
    return result

# Solution 4
from collections import Counter
from itertools import chain
def count_variable(data):
    counts = Counter(data)
    item_iterables = ([item] * count for item, count in counts.items())
    return list(chain.from_iterable(item_iterables))

# Solution 5
from collections import defaultdict
def count_variable(data):
    counts = defaultdict(int)
    for item in data:
        counts[item] += 1
    result = []
    for item, count in counts.items():
        result.extend([item] * count)
    return result
