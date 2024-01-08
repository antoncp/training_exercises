def latest_clock(a, b, c, d):
    digits = sorted([a, b, c, d])
    if 2 in digits and digits[1] < 4 and digits[2] < 6:
        digits.remove(2)
        second = max(filter(lambda x: x < 4, digits))
        digits.remove(second)
        part1 = f"2{second}:"
        print(part1)
    else:
        if 1 in digits:
            first = 1
            digits.remove(1)
        else:
            first = 0
            digits.remove(0)
        second = max(digits)
        digits.remove(second)
        part1 = f"{first}{second}:"
    minute = max(filter(lambda x: x < 6, digits))
    digits.remove(minute)
    return part1 + f"{minute}{digits[0]}"
