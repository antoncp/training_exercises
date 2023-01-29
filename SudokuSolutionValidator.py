def valid_solution(board):
    verticals = [[] for i in range(9)]
    blocks = [[] for i in range(9)]
    for line, row in enumerate(board):
        pos = line//3 * 3
        if len(set(row)) != 9:
            return False
        for x, y in enumerate(row):
            if y == 0:
                return False
            verticals[x].append(y)
            block = pos + (x//3)
            blocks[block].append(y)
    for i in verticals:
        if len(set(i)) != 9:
            return False
    for i in blocks:
        if len(set(i)) != 9:
            return False
    return True
