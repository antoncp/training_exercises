def sort_bubble(arr, prints):
    actions = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
            actions += 1
    if actions != 0:
        print(*arr)
        sort_bubble(arr, prints+1)
    elif prints == 0:
        print(*arr)
    else:
        return


n = int(input())
sort_bubble([int(i) for i in input().split()], 0)
