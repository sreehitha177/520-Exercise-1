# Problem 2: cal_electbill - Chatgpt Cot Solutions
# Task ID: 136
# Description: Write a function to calculate electricity bill.

# Solution 1
def cal_electbill(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return 100 * 1.5 + (units - 100) * 2.5
    elif units <= 500:
        return 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        return 100 * 1.5 + 100 * 2.5 + 300 * 4 + (units - 500) * 6

# Solution 2
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

# Solution 3
def cal_electbill(units):
    bill = 0
    if units > 500:
        bill += (units - 500) * 6
        units = 500
    if units > 200:
        bill += (units - 200) * 4
        units = 200
    if units > 100:
        bill += (units - 100) * 2.5
        units = 100
    bill += units * 1.5
    return bill

# Solution 4
def cal_electbill(units):
    thresholds = [100, 200, 500]
    rates = [1.5, 2.5, 4, 6]
    if units <= thresholds[0]:
        return units * rates[0]
    elif units <= thresholds[1]:
        return 100 * rates[0] + (units - 100) * rates[1]
    elif units <= thresholds[2]:
        return 100 * rates[0] + 100 * rates[1] + (units - 200) * rates[2]
    else:
        return 100 * rates[0] + 100 * rates[1] + 300 * rates[2] + (units - 500) * rates[3]

# Solution 5
def cal_electbill(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return 150 + (units-100)*2.5
    elif units <= 500:
        return 150 + 250 + (units-200)*4
    else:
        return 150+250+1200+(units-500)*6

