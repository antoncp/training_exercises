def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    ver, hor = 0, 0
    for i in walk:
        if i == 'n':
            ver += 1
        elif i == 's':
            ver -= 1
        elif i == 'w':
            hor += 1
        elif i == 'e':
            hor -= 1
    if ver == 0 and hor == 0:
        return True
    else:
        return False
