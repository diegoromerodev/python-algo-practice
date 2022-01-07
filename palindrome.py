def palindrome_helper(str):
    if not str: return ""
    return str[-1] + palindrome_helper(str[0:-1])

def palindrome(str):
    reversed = palindrome_helper(str)
    return str == reversed

print(palindrome("foobar"))