def anagram_check(st1, st2):
    freq_st1 = {}
    freq_st2 = {}

    for char in st1:
        freq_st1[char] = freq_st1.get(char, 0) + 1

    for char in st2:
        freq_st2[char] = freq_st2.get(char, 0) + 1

    for key in freq_st1:
        if key not in freq_st2 or freq_st1[key] != freq_st2[key]:
            return False
    
    return True

print(anagram_check("adc", "cda"))