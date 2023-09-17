def test(r):
    aver = round(sum(r) / len(r), 3)
    high = r.count(10) + r.count(9)
    med = r.count(8) + r.count(7)
    low = len(r) - high - med
    details = {
        'h': high,
        'a': med,
        'l': low,
    }
    return ([aver, details, 'They did well']
            if high == len(r) else [aver, details])
