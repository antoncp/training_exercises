def flick_switch(lst):
    f, result = True, []
    for i in lst:
        if i == 'flick':
            f = not f
        result.append(f)
    return result
