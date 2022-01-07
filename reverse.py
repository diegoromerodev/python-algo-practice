def reverse(str):
    if not str: return ""
    return str[-1] + reverse(str[:-1])

print(reverse("awesome"))