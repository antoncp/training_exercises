def cantor(nested_list):
    new_list = []
    for num, i in enumerate(nested_list):
        if i[num] == 0:
            new_list.append(1)
        else:
            new_list.append(0)
    return new_list
