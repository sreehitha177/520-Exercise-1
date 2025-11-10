# Problem 5: find_tuples - gemini_cot Solution 2
def find_tuples(list_of_tuples, k):
    if k == 0:
        return []
    return [
        tup for tup in list_of_tuples
        if all(element % k == 0 for element in tup)
    ]
