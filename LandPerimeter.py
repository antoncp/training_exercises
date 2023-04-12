def land_perimeter(arr):
    total = 0
    verticals = [[] for i in range(len(arr[0]))]
    for line in arr:
        for num, i in enumerate(list(line)):
            verticals[num].append(i)
            if i == 'X':
                total += 4
                if num != 0 and line[num - 1] == 'X':
                    total -= 2
    for line in verticals:
        for num, i in enumerate(line):
            if i == 'X' and num != 0 and line[num - 1] == 'X':
                total -= 2
    return f'Total land perimeter: {total}'
