def catch_sign_change(lst):
    if len(lst) < 2:
        return 0
    sign = 1 if lst[0] >= 0 else 0
    count = 0
    for i in lst:
        if i < 0:
            if sign:
                count += 1
                sign = 0
        else:
            if not sign:
                count += 1
                sign = 1
    return count
