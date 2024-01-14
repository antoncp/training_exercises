def possibly_perfect(key, answers):
    right, wrong = 0, 0
    for x, y in zip(key, answers):
        if x == "_":
            continue
        elif x == y:
            right += 1
        else:
            wrong += 1
    return True if not right or not wrong else False
