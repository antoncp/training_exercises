def dirReduc(arr):
    op = {"WEST": "EAST", "EAST": "WEST", "NORTH": "SOUTH", "SOUTH": "NORTH"}
    count = {"WEST": [], "EAST": [], "NORTH": [], "SOUTH": []}

    for i, dir in enumerate(arr):
        if count[op[dir]] and count[op[dir]][-1] == max(
            num for sublist in count.values() for num in sublist
        ):
            count[op[dir]].pop()
        else:
            count[dir].append(i)
    return [
        arr[i]
        for i in sorted(num for sublist in count.values() for num in sublist)
    ]
