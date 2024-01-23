def narcissistic(value):
    power = len(str(value))
    all = []
    for i in str(value):
        all.append(int(i)**power)
    return sum(all) == value
