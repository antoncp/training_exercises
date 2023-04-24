def snail(snail_map):
    new_map = []
    while snail_map:
        new_map.extend(snail_map[0])
        snail_map.pop(0)
        for i in snail_map:
            new_map.append(i[-1])
            i.pop()
        if not snail_map:
            break
        new_map.extend(reversed(snail_map[-1]))
        snail_map.pop()
        for i in snail_map[::-1]:
            new_map.append(i[0])
            i.pop(0)
    return new_map
