# Problem 2: cal_electbill - Gemini Self Planning Solutions
# Task ID: 136
# Description: Write a function to calculate electricity bill.

# Note: Solutions extracted from original generated codes file
# See generated_code/original_generated_codes.txt for full Gemini solutions

# Solution 1
def cal_electbill(units):
    if units <= 0:
        return 50.0 # Fixed charge only
    fixed_charge = 50.0
    bill = fixed_charge
    u = units
    
    # Slab 3: Above 300 @ $9.00
    if u > 300:
        slab3_units = u - 300
        bill += slab3_units * 9.00
        u = 300
        
    # Slab 2: 101-300 @ $7.00 (Max 200 units)
    if u > 100:
        slab2_units = u - 100
        bill += slab2_units * 7.00
        u = 100
        
    # Slab 1: 0-100 @ $5.00
    if u > 0:
        bill += u * 5.00
        
    return bill

# Solution 2
def cal_electbill(units):
    if units <= 0:
        return 50.0
    
    fixed_charge = 50.0
    bill = fixed_charge
    
    # Slab 1: 0-100 @ 5.0
    slab1_units = min(units, 100)
    bill += slab1_units * 5.0
    units -= slab1_units
    
    # Slab 2: 101-300 @ 7.0
    if units > 0:
        slab2_units = min(units, 200)
        bill += slab2_units * 7.0
        units -= slab2_units
    
    # Slab 3: >300 @ 9.0
    if units > 0:
        bill += units * 9.0
        
    return bill

# Solution 3
def cal_electbill(units):
    if units <= 0:
        return 50.0
    
    # (max_units_in_slab, rate_per_unit)
    slabs = [(100, 5.00), (200, 7.00), (float('inf'), 9.00)]
    
    bill = 50.0 # Fixed Charge
    remaining_units = units
    
    for max_in_slab, rate in slabs:
        if remaining_units <= 0:
            break
            
        if max_in_slab == float('inf'):
            units_to_charge = remaining_units
        else:
            units_to_charge = min(remaining_units, max_in_slab)
            
        bill += units_to_charge * rate
        remaining_units -= units_to_charge
        
    return bill

# Solution 4
def cal_electbill(units):
    if units <= 0:
        return 50.0
    
    bill = 50.0 
    
    if units <= 100:
        bill += units * 5.0
    elif units <= 300:
        # 100 units at 5.0 + remaining at 7.0
        bill += 100 * 5.0
        bill += (units - 100) * 7.0
    else:
        # 100 units at 5.0 + 200 units at 7.0 + remaining at 9.0
        bill += 100 * 5.0
        bill += 200 * 7.0
        bill += (units - 300) * 9.0
        
    return bill

# Solution 5
def cal_electbill(units):
    if units <= 0:
        return 50.0
    
    bill = 50.0
    
    # Calculate costs for units > 300 at $9.00
    bill += max(0, units - 300) * 9.0
    
    # Calculate costs for units 101-300 at $7.00
    # The max(0, units - 100) is the total over 100.
    # We subtract max(0, units - 300) to only count the 101-300 block.
    slab2_units = max(0, units - 100) - max(0, units - 300)
    bill += slab2_units * 7.0
    
    # Calculate costs for units 0-100 at $5.00
    slab1_units = min(units, 100)
    bill += slab1_units * 5.0
    
    return bill