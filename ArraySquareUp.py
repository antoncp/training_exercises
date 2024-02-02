def square_up(n):
    result = []
    for i in range(1, n + 1):
        pre_result = []
        for x in range(1, n + 1):
            pre_result.append(x if x <= i else 0)
        result.extend(pre_result[::-1])
    return result
