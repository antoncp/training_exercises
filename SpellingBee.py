def how_many_bees(hive):
    result = 0
    if not hive:
        return result
    for line in hive:
        l = "".join(line)
        result += l.count("bee")
        result += l[::-1].count("bee")
    vertical = []
    for i in range(len(hive[0])):
        new_line = []
        for line in hive:
            new_line.append(line[i])
        vertical.append(new_line)
    for line in vertical:
        l = "".join(line)
        result += l.count("bee")
        result += l[::-1].count("bee")
    return result
