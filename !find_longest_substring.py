def find_longest_substring(str):
    seen = {}
    longest = 0
    start = 0
    for i in range(len(str)):
        char = str[i]
        if seen[char]:
            start = max(start, seen[char])
        longest = max(longest, i - start + 1)
        seen[char] = i + 1
    return longest