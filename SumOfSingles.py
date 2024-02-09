def repeats(arr):
    return sum([i for i in set(arr) if arr.count(i) == 1])
