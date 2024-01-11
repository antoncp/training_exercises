def averages(arr):
    if arr and len(arr) > 1:
        return [(x+y)/2 for x, y in zip(arr, arr[1:])]
    return []
