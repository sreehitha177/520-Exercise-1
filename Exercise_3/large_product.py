def large_product(list1, list2, n):
    if not list1 or not list2:
        return []    
    products = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            prod = list1[i] * list2[j]
            products.append(prod)    

    products.sort(reverse=True)
    
    if n <= 0:
        return []
    elif n > len(products):
        n = len(products) - 1
    
    result = []
    for k in range(n):
        result.append(products[k])
    
    return result
