def naive_string_search(str1, str2):
    count = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i+j] != str2[j]:
                break
            if j == len(str2) - 1:
                count +=1
    return count

print(naive_string_search("hehello", "he"))