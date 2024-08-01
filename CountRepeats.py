def count_repeats(txt):
    repeats = 0
    for num, i in enumerate(txt[1:], start=1):
        if i == txt[num-1]:
            repeats += 1
    return repeats
