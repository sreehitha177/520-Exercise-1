# Problem 2: cal_electbill - chatgpt_cot Solution 2
def cal_electbill(units):
    slabs = [(100, 1.5), (100, 2.5), (300, 4), (float('inf'), 6)]
    total = 0
    for limit, rate in slabs:
        if units > limit:
            total += limit * rate
            units -= limit
        else:
            total += units * rate
            break
    return total
