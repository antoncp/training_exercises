import heapq


def k_difference(n, areas, k):
    differences = []
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(areas[i] - areas[j])
            heapq.heappush(differences, diff)
            if len(differences) > k:
                heapq.heappop(differences)
    return heapq.heappop(differences)


n = int(input())
areas = list(map(int, input().split()))
k = int(input())
print(k_difference(n, areas, k))
