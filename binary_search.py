def binary_search(lst, el):
    left = 0
    mid = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == el: return mid
        elif lst[mid] < el: left = mid + 1
        else: right = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5], 3))