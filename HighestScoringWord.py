def high(x):
    results = []
    for w in x.split():
        points = sum(ord(l) - 96 for l in w)
        results.append((points, w))
    results = sorted(results, key=lambda x: x[0], reverse=True)
    return results[0][1]
