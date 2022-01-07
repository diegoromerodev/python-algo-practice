def same_frequency(num1, num2):
    str1 = str(num1)
    str2 = str(num2)
    freq = {}

    for char in str1:
        freq[char] = freq.get(char, 0) + 1
    
    for char in str2:
        if not freq.get(char, 0):
            return False
        freq[char] -= 1
    
    return True

print(same_frequency(828,828))