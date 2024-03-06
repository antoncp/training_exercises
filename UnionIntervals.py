def interval_insert(myl, interval):
    new_myl = []
    for i in myl:
        if i[0] >= interval[0] and i[1] <= interval[1]:
            pass
        elif i[0] < interval[0] <= i[1] or i[0] <= interval[1] < i[1]:
            interval = (min(i[0], interval[0]), max(i[1], interval[1]))
        else:
            new_myl.append(i)
    return sorted(new_myl + [interval])
