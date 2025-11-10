# Problem 2: cal_electbill - chatgpt_self_planning Solution 2
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
