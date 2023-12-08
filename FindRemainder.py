def remainder(a,b):
    first = max(a, b)
    second = min(a, b)
    if second == 0:
        return None
    if first == 0:
        return 0
    return first % second
