def get_middle(s):
    l = len(s)
    if l < 3:
        return s
    if l % 2 == 0:
        return s[int(l/2-1):int(l/2+1)]
    return s[int(l//2):int(l//2+1)]
