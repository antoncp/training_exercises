def binarySearch(arr, x, left, right):
    if right <= left and left != 0:
        return -1
    mid = (left + right) // 2
    target = int(arr[mid])
    print(mid, target)
    if target >= x and (int(arr[mid-1]) < x or mid == 0):
        return mid + 1
    elif x <= target:
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


scope = int(input())
arr = input().split()
bike_price = int(input())
res_1 = binarySearch(arr, bike_price, 0, scope)
res_2 = binarySearch(arr, bike_price*2, 0, scope)
print(f"{res_1} {res_2}")
