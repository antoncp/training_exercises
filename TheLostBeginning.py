def find(s):
    size = len(s)
    for n in range(1, size // 2 + 1):
        start = int(s[:n])
        current = start
        i = n
        while i < size:
            expected = str(current + 1)
            if not s.startswith(expected, i):
                break
            i += len(expected)
            current += 1
        if i == size:
            return start
    return int(s)
