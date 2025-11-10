# Problem 7: extract_elements - Gemini Self Planning Solutions
# Task ID: 898
# Description: Write a function to extract specified number of elements from a given list, which follow each other continuously.

# Solution 1
def extract_elements(lst, n):
    if n <= 0 or n > len(lst):
        return []
    max_start_index = len(lst) - n
    return [
        lst[i : i + n] 
        for i in range(max_start_index + 1)
    ]

# Solution 2
def extract_elements(lst, n):
    if n <= 0 or n > len(lst):
        return []
    result = []
    max_start_index = len(lst) - n
    for i in range(max_start_index + 1):
        sub_list = lst[i : i + n]
        result.append(sub_list)
    return result

# Solution 3
def extract_elements(lst, n):
    if n <= 0 or n > len(lst):
        return []
    # Create n slices, each shifted by one element
    slices = (lst[i:] for i in range(n))
    # zip combines the first element of each slice, then the second, etc.
    return [list(tup) for tup in zip(*slices)]

# Solution 4
def extract_elements(lst, n):
    if n <= 0 or n > len(lst):
        return []
    
    def window_generator(data, size):
        for i in range(len(data) - size + 1):
            yield data[i:i + size]
            
    # Return as a list as the function signature implies a full list return
    return list(window_generator(lst, n))

# Solution 5
from itertools import islice
def extract_elements(lst, n):
    if n <= 0 or n > len(lst):
        return []
        
    result = []
    data_iterator = iter(lst)
    
    # Create iterators for each starting position
    teed_iterators = [islice(data_iterator, i, None) for i in range(n)]
    
    # Use zip to combine the elements from each starting position
    # The length of the shortest iterator (the last one) determines the number of windows
    for window_tuple in zip(*teed_iterators):
        result.append(list(window_tuple))
        
    return result