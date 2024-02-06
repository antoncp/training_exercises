def find_missing_letter(chars):
    control_list = list(map(chr, range(97, 123)))
    start = control_list.index(chars[0].lower())
    for x, y in zip(chars, control_list[start:]):
        if x.lower() != y:
            return y if x.islower() else y.upper()
