def find_routes(routes):
    nums = len(routes)
    first = [i[0] for i in routes]
    second = [i[1] for i in routes]
    result = []
    for i in range(nums):
        if first[i] not in second:
            result.append(first[i])
            result.append(second[i])
            break
    while len(result) < nums + 1:
        idx = first.index(result[-1])
        result.append(second[idx])
    return ", ".join(result)
