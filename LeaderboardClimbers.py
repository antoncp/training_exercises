def leaderboard_sort(leaderboard, changes):
    for i in changes:
        name, move = i.split()
        cur_pos = leaderboard.index(name)
        if move[:1] == '+':
            new_pos = cur_pos-int(move[1:])
        else:
            new_pos = cur_pos+int(move[1:])
        leaderboard.pop(cur_pos)
        leaderboard = leaderboard[:new_pos] + [name] + leaderboard[new_pos:]
    return leaderboard
