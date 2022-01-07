def min_subarray_len(lst, target):
    total = 0
    start = 0
    end = 0
    min_len = None

    while start < len(lst):
        if total < target and end < len(lst):
            total += lst[end]
            end += 1
        elif total >= target:
            if min_len is None: min_len = end - start
            min_len = min(min_len, end - start)
            total -= lst[start]
            start += 1
        else:
            break
    
    if min_len is None: return 0
    return min_len

print(min_subarray_len([2,3,1,2,4,3], 7))