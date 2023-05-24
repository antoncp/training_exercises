rows = int(input())
columns = int(input())
matrix = []
for i in range(rows):
    matrix.append(list(input().split()))
row = int(input())
column = int(input())
pos = [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]
pos = filter(lambda x: x[0] >= 0
             and x[0] < rows
             and x[1] >= 0
             and x[1] < columns, pos)
result = []
for i in pos:
    result.append(int(matrix[i[0]][i[1]]))
output = map(str, sorted(result))
print(' '.join(output))
