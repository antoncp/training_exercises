def getHint(secret: str, guess: str) -> str:
    bulls, cows = 0, 0
    cows_secret, cows_guess = [0 for i in range(10)], [0 for i in range(10)]
    for x, y in zip(secret, guess):
        if x == y:
            bulls += 1
        else:
            cows_secret[int(x)] += 1
            cows_guess[int(y)] += 1
    for cow_1, cow_2 in zip(cows_secret, cows_guess):
        if cow_1 and cow_2:
            cows += min(cow_1, cow_2)
    return f'{bulls}A{cows}B'
