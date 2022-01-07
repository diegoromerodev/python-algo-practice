def are_there_duplicates(*args):
    freq = {}
    for item in args:
        if item in freq:
            return True
        freq[item] = 1
    
    return False

print(are_there_duplicates(1,2,2,3))