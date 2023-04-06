def score(dice):
    AWARDS = {
        1: 1000,
        2: 200,
        3: 300,
        4: 400,
        5: 500,
        6: 600
    }
    result = 0
    for i in range(1, 6):
        if dice.count(i) >= 3:
            result += AWARDS[i]
            for r in range(3):
                dice.remove(i)

    for i in dice:
        if i == 1:
            result += 100
        if i == 5:
            result += 50

    return result
