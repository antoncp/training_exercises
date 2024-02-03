def solution(*args):
    arr = [i for i in args]
    return len(arr) != len(set(arr))
