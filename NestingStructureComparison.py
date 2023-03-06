def same_structure_as(original, other):
    one = []
    two = []
    if isinstance(original, list):
        for i in nested(original):
            one.append(i)
    else:
        one = original
    if isinstance(other, list):
        for i in nested(other):
            two.append(i)
    else:
        two = other
    return one == two


def nested(lst):
    if not isinstance(lst, list):
        yield 0
    for i in lst:
        if isinstance(i, list):
            yield 1
            yield from nested(i)
        else:
            yield 0
