def count_unique_values(arr):
    low = 0
    max = 1
    unique_values = 1

    if len(arr) == 0: return low

    while max < len(arr) and low < max:
        if arr[low] != arr[max]:
            unique_values += 1
        low += 1
        max += 1

    return unique_values

print(count_unique_values([1]))