# Problem 2: cal_electbill - gemini_self_planning Solution 2
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
