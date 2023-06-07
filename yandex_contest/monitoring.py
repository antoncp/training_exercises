rows = int(input())
columns = int(input())
matrix = []
for i in range(rows):
    matrix.extend(list(input().split()))
for i in range(columns):
    print(*matrix[i::columns])
