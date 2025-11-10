# Problem 8: lcopy - gemini_cot Solution 2
def lcopy(tup):
    if not isinstance(tup, tuple) or len(tup) != 1:
        return None
    list_to_copy = tup[0]
    if not isinstance(list_to_copy, list):
        return None
    copied_list = list_to_copy[:]
    return copied_list
