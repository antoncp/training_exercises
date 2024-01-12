def getting_mad(arr):
    if len(arr) != len(set(arr)):
        return 0
    dif = []
    arr = sorted(arr)
    for x, y in zip(arr, arr[1:]):
        dif.append(abs(x-y))
    return min(dif)
