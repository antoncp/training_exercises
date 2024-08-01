def unique_in_order(sequence):
    if sequence:
        new_list = [sequence[0]]
        for i in sequence[1:]:
            if new_list[-1] != i:
                new_list.append(i)
    return new_list if sequence else []
