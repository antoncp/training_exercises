def two_are_positive(a, b, c):
    count = 0
    nums = [a, b, c]
    for i in nums:
        if i > 0:
            count += 1
    return count == 2
