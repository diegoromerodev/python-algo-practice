def bubble_sort(usr_lst):
    lst = usr_lst.copy()
    sorting = False
    for i in reversed(range(len(lst))):
        sorting = False
        for j in range(i - 1):
            if lst[j] > lst[j + 1]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
                sorting = True
        if not sorting: break
    return lst

print(bubble_sort([10,1,2,3,4,5,6,7,8,9,10]))