def max_subarray_sum(lst, length):
    if(len(lst) < length): return None
    max_sum = 0
    for i in range(length):
        max_sum += lst[i]
    
    tmp = max_sum
    i = length
    while i < len(lst):
        tmp = tmp - lst[i - length] + lst[i]
        max_sum = max(tmp, max_sum)
        i += 1
    
    return max_sum

print(max_subarray_sum([2,9,3,7,4], 4))