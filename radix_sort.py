import math
from typing import List

def get_num(num, pos):
    exponent = 10 ** pos
    divider = (10 * exponent)
    return abs(num) % divider // exponent

def digit_count(num):
    if num == 0: return 1
    return math.floor(math.log10(abs(num))) + 1

def most_digits(lst):
    return digit_count(max(lst))

def radix_sort(lst):
    buckets = []
    result = lst

    for i in range(most_digits(lst)):
        buckets = []

        for j in range(10):
            buckets.append([])

        for k in range(len(lst)):
            to_bucket =  get_num(result[k], i)
            buckets[to_bucket].append(result[k])
        
        result = []

        for b in buckets:
            result += b

    return result

print(radix_sort([1, 123, 4, 267, 5555]))