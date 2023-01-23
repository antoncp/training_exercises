def is_pangram(s):
    return len(set([i.lower() for i in s if i.isalpha()])) == 26
