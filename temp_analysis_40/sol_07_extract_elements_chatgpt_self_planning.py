# Problem 7: extract_elements - chatgpt_self_planning Solution 2
def extract_elements(lst,n):
    res=[]
    for i in range(len(lst)-n+1): res.append(lst[i:i+n])
    return res
