# Problem 2: cal_electbill - Chatgpt Self Planning Solutions
# Task ID: 136
# Description: Write a function to calculate electricity bill.

# Solution 1
def cal_electbill(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return 100*1.5 + (units-100)*2.5
    elif units <= 500:
        return 100*1.5 + 100*2.5 + (units-200)*4
    else:
        return 100*1.5 + 100*2.5 + 300*4 + (units-500)*6

# Solution 2
def cal_electbill(units):
    slabs=[(100,1.5),(100,2.5),(300,4),(float('inf'),6)]
    total=0
    for s,r in slabs:
        if units>s:
            total+=s*r
            units-=s
        else:
            total+=units*r
            break
    return total

# Solution 3
def cal_electbill(units):
    bill=0
    if units>500:
        bill+=(units-500)*6
        units=500
    if units>200:
        bill+=(units-200)*4
        units=200
    if units>100:
        bill+=(units-100)*2.5
        units=100
    bill+=units*1.5
    return bill

# Solution 4
def cal_electbill(units):
    t=[100,200,500]
    r=[1.5,2.5,4,6]
    if units<=t[0]: return units*r[0]
    elif units<=t[1]: return 100*r[0]+(units-100)*r[1]
    elif units<=t[2]: return 100*r[0]+100*r[1]+(units-200)*r[2]
    else: return 100*r[0]+100*r[1]+300*r[2]+(units-500)*r[3]

# Solution 5
def cal_electbill(units):
    bill=0
    for u,r in [(100,1.5),(100,2.5),(300,4)]:
        if units>u:
            bill+=u*r
            units-=u
        else:
            bill+=units*r
            return bill
    bill+=units*6
    return bill

