def k_difference(n, areas, k):
    differences = []
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(areas[i] - areas[j])
            differences.append(diff)
    differences.sort()
    return differences[k - 1]


n = int(input())
areas = list(map(int, input().split()))
k = int(input())
print(k_difference(n, areas, k))
