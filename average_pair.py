def average_pair(lst, target):
    start = 0
    end = len(lst) - 1

    while start < end:
        avg = (lst[start] + lst[end]) / 2
        if avg == target: return True
        elif avg > target:
            end -= 1
        else: start += 1

    return False

print(average_pair([-1, 0, 3, 4, 5, 6], 5))