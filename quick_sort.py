def partition(arr, start=0, end=None):
    if end is None: end = len(arr)
    compared = arr[start]
    position = start
    for i in range(start + 1, end):
        if arr[i] < compared:
            position += 1
            temp = arr[position]
            arr[position] = arr[i]
            arr[i] = temp

    arr[start] = arr[position]
    arr[position] = compared
    return position

def quick_sort(arr, start=0, end=None):
    if end is None: end = len(arr)
    if(end-start < 1): return arr
    sorted_to = partition(arr, start, end)
    quick_sort(arr, start, sorted_to - 1)
    quick_sort(arr, sorted_to + 1, end)
    return arr


print(quick_sort([20,9,2,5,10,21,50,5,80]))