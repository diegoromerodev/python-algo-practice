def power(num, base):
    if base == 0: return 1
    return num * power(num, base-1)

print(power(2, 4))