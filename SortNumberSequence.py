def sort_sequence(sequence):
    new_s, sub_s = [], []
    for i in sequence:
        if i == 0:
            new_s.append(sorted(sub_s) + [0])
            sub_s = []
        else:
            sub_s.append(i)
    return sum(sorted(new_s, key=lambda x: sum(x)), [])
