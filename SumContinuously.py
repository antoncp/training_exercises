def add(lst):
    new_list = [lst[0]]
    cur_sum = lst[0]
    for i in lst[1:]:
        new_list.append(cur_sum+i)
        cur_sum += i
    return new_list