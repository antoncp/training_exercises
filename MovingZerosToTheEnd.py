def move_zeros(lst):
    zeros = [0 for i in range(lst.count(0))]
    final = filter(lambda x: x != 0, lst)
    return list(final) + zeros
