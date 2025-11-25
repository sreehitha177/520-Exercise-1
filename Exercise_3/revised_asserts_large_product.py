# spec1
if not list1 or not list2 or n <= 0: 
    assert len(res) == 0; 
else:
    assert len(res) == min(n, len(list1)*len(list2))

# spec2
assert all(any(res[k] == list1[i] * list2[j]
               for i in range(len(list1))
               for j in range(len(list2)))
           for k in range(len(res)))

# spec3
assert all(res[i] >= res[i+1] for i in range(len(res)-1))

# spec4
if len(res) > 0:
    min_in_res = res[-1]
    assert all((list1[i] * list2[j]) <= min_in_res
               or (list1[i] * list2[j]) in res
               for i in range(len(list1))
               for j in range(len(list2)))
else:
    assert n <= 0 or len(list1) == 0 or len(list2) == 0


# spec5
if n > 0 and len(list1) > 0 and len(list2) > 0:
    max_product = max(list1[i] * list2[j]
                      for i in range(len(list1))
                      for j in range(len(list2)))
    assert res[0] == max_product

