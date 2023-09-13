def create_iterator(func, n):
    def inner_iterator(x):
        p = n
        result = x
        while p > 0:
            p -= 1
            result = func(result)
        return result
    return inner_iterator
