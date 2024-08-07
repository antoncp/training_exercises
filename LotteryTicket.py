def bingo(ticket, win):
    wins = 0
    for t in ticket:
        for l in t[0]:
            if ord(l) == t[1]:
                wins += 1
                break
    return 'Loser!' if wins < win else 'Winner!'
