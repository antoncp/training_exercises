def greatest_distance(arr):
    options = {}
    for i in arr:
        if i not in options and arr.count(i) > 1:
            start = arr.index(i)
            end = list(reversed(arr)).index(i)
            distance = len(arr) - start - 1 - end
            options[i] = distance
    return max(options.values()) if options else 0
