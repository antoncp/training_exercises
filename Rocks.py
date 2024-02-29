def rocks(n):
    if n < 10:
        return n
    result = 0
    while n > 9:
        cur = n - (rest := int((len(str(n)) - 1) * "9"))
        result += cur * len(str(n))
        n = rest
    return result + 9
