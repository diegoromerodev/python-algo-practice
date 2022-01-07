def merge(n, m):
    i = 0
    j = 0
    srtd = []
    while i < len(n) and j < len(m):
        if n[i] < m[j]:
            srtd.append(n[i])
            i += 1
        else:
            srtd.append(m[j])
            j += 1

    while i < len(n):
        srtd.append(n[i])
        i += 1

    while j < len(m):
        srtd.append(m[j])
        j += 1

    print(srtd)
    return srtd

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    half = len(lst) // 2
    left = merge_sort(lst[:half])
    right = merge_sort(lst[half:])
    return merge(left, right)

#print(sort([1,3,4,6,2,9,7]))
print(merge_sort([2,10,19,20,5,3,7]))