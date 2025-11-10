# Problem 2: cal_electbill - gemini_cot Solution 2
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
