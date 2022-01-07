def selection_sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        if min != i:
            lst[min], lst[i] = lst[i], lst[min]
    return lst

print(selection_sort([1, 2, 3, 7, 5, 2, 1, 6]))