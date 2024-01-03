def nearestPalindromic(n):
    low, high, int_n = int(n), int(n), int(n)
    size = len(n)
    if size < 5:
        while True:
            low -= 1
            if str(low) == str(low)[::-1]:
                return str(low)
            high += 1
            if str(high) == str(high)[::-1]:
                return str(high)
    if int(n[0]) == 1 and int(n[1:]) < 2:
        return "9" * (size - 1)
    if n.count("9") == size:
        return str(int(n) + 2)
    mid = int(n[size // 2])
    start = n[: size // 2]
    start_even = n[: size // 2 - 1]
    end = n[size // 2 - 1 :: -1]
    end_even = n[size // 2 - 2 :: -1]
    if n == n[::-1]:
        mid = mid - 1 if mid > 0 else mid + 1
        if size % 2 == 0:
            return start_even + str(mid) + str(mid) + end_even
        else:
            return start + str(mid) + end
    if size % 2 == 0:
        mid = int(n[size // 2 - 1])
        ans1 = start_even + str(mid) + str(mid) + end_even
        ans2 = start_even + str(mid + 1) + str(mid + 1) + end_even
        ans3 = start_even + str(abs(mid - 1)) + str(abs(mid - 1)) + end_even
    else:
        ans1 = start + str(mid) + end
        ans2 = start + str(mid + 1) + end
        ans3 = start + str(abs(mid - 1)) + end
    return min(
        (abs(int_n - int(ans1)), ans1),
        (abs(int_n - int(ans2)), ans2),
        (abs(int_n - int(ans3)), ans3),
    )[1]
