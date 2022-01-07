def product_list(lst):
    if not len(lst): return 1
    return lst[0] * product_list(lst[1:])

print(product_list([1,2,3]))