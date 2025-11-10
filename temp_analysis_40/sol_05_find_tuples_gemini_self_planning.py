# Problem 5: find_tuples - gemini_self_planning Solution 2
def find_tuples(list_of_tuples, k):
    if k == 0:
        return []
    return list(filter(lambda tup: all(e % k == 0 for e in tup), list_of_tuples))
