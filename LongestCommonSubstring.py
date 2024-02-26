def longest(string1, string2):
    long = ""
    for n, i in enumerate(string1):
        if i in string2:
            sub = i
            idx = n
            while sub in string2:
                try:
                    sub += string1[idx + 1]
                except:
                    break
                idx += 1
            if len(sub[:-1]) > len(long):
                long = sub[:-1]
    return long.strip()
