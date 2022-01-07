#O(n) -> O(2n) || O(n)
def same(arr1, arr2):
    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)
    is_same = True
    
    if sum(sorted_arr1) < sum(sorted_arr2):
        pass
    elif sum(sorted_arr1) > sum(sorted_arr2):
        sorted_arr1, sorted_arr2 = [sorted_arr2, sorted_arr1]

    if len(sorted_arr1) == len(sorted_arr2) and is_same:
        for i in range(len(sorted_arr1)):
            if sorted_arr1[i] ** 2 != sorted_arr2[i]:
                is_same = False

    if is_same: return True
    else: return False

print(same([1,4,3], [4,1,9]))