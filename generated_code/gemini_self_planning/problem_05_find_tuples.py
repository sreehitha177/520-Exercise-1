# Problem 5: find_tuples - Gemini Self Planning Solutions
# Task ID: 75
# Description: Write a function to find tuples which have all elements divisible by k from the given list of tuples.

# Solution 1
def find_tuples(list_of_tuples, k):
    if k == 0:
        return []
    return [
        tup for tup in list_of_tuples 
        if all(element % k == 0 for element in tup)
    ]

# Solution 2
def find_tuples(list_of_tuples, k):
    if k == 0:
        return []
    return list(filter(lambda tup: all(e % k == 0 for e in tup), list_of_tuples))

# Solution 3
def find_tuples(list_of_tuples, k):
    if k == 0:
        return []
    result = []
    for tup in list_of_tuples:
        is_divisible = True
        for element in tup:
            if element % k != 0:
                is_divisible = False
                break
        if is_divisible:
            result.append(tup)
    return result

# Solution 4
def find_tuples(list_of_tuples, k):
    if k == 0:
        return []
    # Generator expression yields tuples that satisfy the condition
    divisible_tuples = (
        tup for tup in list_of_tuples 
        if all(e % k == 0 for e in tup)
    )
    return list(divisible_tuples)

# Solution 5
def find_tuples(list_of_tuples, k):
    if k == 0:
        return []
    result = []
    for tup in list_of_tuples:
        # Check all elements. Loop breaks and executes else if no break occurs.
        for element in tup:
            if element % k != 0:
                break
        else:
            # Executes if the inner loop completes without a break
            result.append(tup)
    return result
