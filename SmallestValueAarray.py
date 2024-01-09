def find_smallest(numbers, to_return):
    val = min(numbers)
    if to_return == "index":
        return numbers.index(val)
    return val
