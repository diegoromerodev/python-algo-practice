def is_subsequence(sub, str):
    subidx = 0
    stridx = 0
    while stridx < len(str):
        if sub[subidx] == str[stridx]:
            subidx += 1
        if subidx == len(sub): return True
        stridx += 1
    return False



print(is_subsequence("hello", "hello world"))