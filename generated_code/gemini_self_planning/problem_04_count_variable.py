# Problem 4: count_variable - Gemini Self Planning Solutions
# Task ID: 810
# Description: Write a function to iterate over elements repeating each as many times as its count.

# Solution 1
from collections import Counter
def count_variable(data):
    # Counter maintains order of insertion from Python 3.7+
    counts = Counter(data)
    final_output = []
    for element, count in counts.items():
        final_output.extend([element] * count)
    return final_output

# Solution 2
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

# Solution 3
from collections import Counter
from itertools import chain
def count_variable(data):
    counts = Counter(data)
    # Generator creates iterables like [item, item, ...], one for each unique item
    item_iterables = ([item] * count for item, count in counts.items())
    # Flatten the iterables into a single list
    return list(chain.from_iterable(item_iterables))

# Solution 4
def count_variable(data):
    result = []
    seen = set()
    for item in data:
        if item not in seen:
            count = data.count(item)
            result.extend([item] * count)
            seen.add(item)
    return result

# Solution 5
from collections import Counter
def count_variable(data):
    counts = Counter(data)
    items = list(counts.items())
    
    # If the user expects a specific order (e.g., sorted by item value), use sort.
    # Assuming order by first appearance is preferred, but using list sort for distinction
    # If using list(counts.items()), the order is usually insertion order (3.7+)
    
    final_output = []
    for element, count in items:
        final_output.extend([element] * count)
    return final_output