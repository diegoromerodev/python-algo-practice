def is_odd(num): return num % 2 != 0

def some_recursive(lst, fn):
    if not len(lst): return False
    elif not fn(lst[0]): return some_recursive(lst[1:], fn)
    return True

print(some_recursive([1,2,3,4], is_odd))