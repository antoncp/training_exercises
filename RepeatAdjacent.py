def repeat_adjacent(st):
    last_group, supergroup = None, False
    count = 0
    for i, letter in enumerate(st[1:], 1):
        if letter == st[i - 1]:
            if last_group and i - last_group < 3 and st[last_group] != letter:
                supergroup = True
            last_group = i
        elif last_group and i - last_group == 2 and supergroup:
            count += 1
            supergroup = False
    return count if not supergroup else count + 1
