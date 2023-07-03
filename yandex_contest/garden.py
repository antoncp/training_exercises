n = int(input())
segments = []

for _ in range(n):
    start, end = map(int, input().split())
    segments.append([start, end])

segments.sort(key=lambda x: x[0])

result = []

for segment in segments:
    if not result or result[-1][1] < segment[0]:
        result.append(segment)
    else:
        result[-1][1] = max(result[-1][1], segment[1])

for segment in result:
    print(segment[0], segment[1])
