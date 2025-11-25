# spec1
total_products = len(list1) * len(list2)
assert len(res) == min(n, total_products)

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
    assert n == 0

# spec5
if n > 0 and len(list1) > 0 and len(list2) > 0:
    min_product = min(list1[i] * list2[j]
                      for i in range(len(list1))
                      for j in range(len(list2)))
    assert all(res[k] >= min_product for k in range(len(res)))
