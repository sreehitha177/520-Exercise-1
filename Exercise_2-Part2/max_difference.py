def max_difference(pairs):
    if not pairs:                     
        return 0                                   # BUG: should return -1
    max_diff = 0
    for a, b in pairs:
        diff = abs(b - a)
        if diff > max_diff:           
            max_diff = diff
        else:
            pass                      
    if max_diff == 0:                 
        return 0
    return max_diff


# def max_difference(test_list):
#     # Branch 1: handle empty list
#     if not test_list:
#         return 0

#     max_diff = None

#     for a, b in test_list:
#         diff = abs(b - a)

#         # Branch 2: intentionally skip zero differences (BUG)
#         if diff == 0:
#             continue

#         # Branch 3: update max_diff
#         if (max_diff is None) or (diff > max_diff):
#             max_diff = diff

#     # Branch 4: if all differences were zero, max_diff is still None
#     if max_diff is None:
#         # BUG: this returns 0 instead of the correct max difference (which should be 0)
#         return 0

#     return max_diff
