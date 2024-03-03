def solve(arr):
    arr_dict = {}
    for i in arr:
        if arr_dict.get(i):
            arr_dict[i] += 1
        else:
            arr_dict[i] = 1
    f_sort = sorted(arr_dict.items(), key=lambda x: (-x[1], x[0]))
    f_arr = []
    for val, rep in f_sort:
        for i in range(rep):
            f_arr.append(val)
    return f_arr
