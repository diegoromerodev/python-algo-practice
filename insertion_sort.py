def insertion_sort(lst):
    for i in range(1, len(lst)):
        curr_val = lst[i]
        curr_idx = i;
        for j in reversed(range(i)):
            lst[curr_idx] = lst[j]
            if curr_val > lst[j]: break
            curr_idx = j
        lst[curr_idx] = curr_val
    return lst

print(insertion_sort([6,1,2,5,20]))