def validate_battlefield(field):
    field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for line in field:
        line.append(0)
    fleet = {1: 0, 2: 0, 3: 0, 4: 0}
    ideal_fleet = {1: 8, 2: 3, 3: 2, 4: 1}
    verticals = [[] for i in range(11)]
    for num_line, line in enumerate(field):
        ship = 0
        for num_i, i in enumerate(line):
            verticals[num_i].append(i)
            if (
                i == 1
                and field[num_line + 1][num_i] == 0
                and field[num_line - 1][num_i] == 0
                and field[num_line - 1][num_i - 1] == 0
                and field[num_line + 1][num_i - 1] == 0
                and field[num_line - 1][num_i + 1] == 0
                and field[num_line + 1][num_i + 1] == 0
            ):
                ship += 1
            else:
                if 0 < ship < 5:
                    fleet[ship] += 1
                ship = 0
    for num_line, line in enumerate(verticals):
        ship = 0
        for num_i, i in enumerate(line):
            if (
                i == 1
                and verticals[num_line + 1][num_i] == 0
                and verticals[num_line - 1][num_i] == 0
                and verticals[num_line - 1][num_i - 1] == 0
                and verticals[num_line + 1][num_i - 1] == 0
                and verticals[num_line - 1][num_i + 1] == 0
                and verticals[num_line + 1][num_i + 1] == 0
            ):
                ship += 1
            else:
                if 0 < ship < 5:
                    fleet[ship] += 1
                ship = 0
    return fleet == ideal_fleet
