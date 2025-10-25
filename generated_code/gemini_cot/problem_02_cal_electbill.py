# Problem 2: cal_electbill - Gemini Cot Solutions
# Task ID: 136
# Description: Write a function to calculate electricity bill.


# Solution 1
def cal_electbill(units):
    if units <= 0:
        return 50.0
    fixed_charge = 50.0
    bill = fixed_charge
    remaining_units = units
    if remaining_units > 100:
        bill += 100 * 5.00
        remaining_units -= 100
    else:
        bill += remaining_units * 5.00
        return bill
    if remaining_units > 200:
        bill += 200 * 7.00
        remaining_units -= 200
    else:
        bill += remaining_units * 7.00
        return bill
    bill += remaining_units * 9.00
    return bill

# Solution 2
def cal_electbill(units):
    if units <= 0:
        return 50.0
    fixed_charge = 50.0
    bill = fixed_charge
    if units <= 100:
        bill += units * 5.0
    elif units <= 300:
        bill += 100 * 5.0
        bill += (units - 100) * 7.0
    else:
        bill += 100 * 5.0
        bill += 200 * 7.0
        bill += (units - 300) * 9.0
    return bill

# Solution 3
def cal_electbill(units):
    if units <= 0:
        return 50.0
    fixed_charge = 50.0
    bill = fixed_charge
    slabs = [
        (100, 5.00, 0),
        (300, 7.00, 100),
        (float('inf'), 9.00, 300)
    ]
    remaining_units = units
    for limit, rate, prev_limit in slabs:
        if remaining_units > 0:
            slab_width = limit - prev_limit
            if units <= limit:
                units_in_slab = remaining_units
                bill += units_in_slab * rate
                remaining_units = 0
            else:
                bill += slab_width * rate
                remaining_units -= slab_width
        else:
            break
    return bill

# Solution 4
def cal_electbill(units):
    if units <= 0:
        return 50.0
    fixed_charge = 50.0
    bill = fixed_charge
    u = units
    if u > 300:
        slab3_units = u - 300
        bill += slab3_units * 9.00
        u = 300
    if u > 100:
        slab2_units = u - 100
        bill += slab2_units * 7.00
        u = 100
    if u > 0:
        slab1_units = u
        bill += slab1_units * 5.00
    return bill

# Solution 5
def cal_electbill(units):
    if units <= 0:
        return 50.0
    fixed_charge = 50.0
    bill = fixed_charge
    slab1_units = min(units, 100)
    bill += slab1_units * 5.0
    units -= slab1_units
    if units > 0:
        slab2_limit = 200
        slab2_units = min(units, slab2_limit)
        bill += slab2_units * 7.0
        units -= slab2_units
    if units > 0:
        bill += units * 9.0
    return bill

