def flatten(lst):
    new_list = []
    if not len(lst): return new_list
    return new_list.append(lst[0]) + flatten(lst[1:])

print(flatten([1,2,3,[4,5]]))