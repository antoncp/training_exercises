def max_triangle_perimeter(n, sides):
    sides.sort(reverse=True)  
    for i in range(n - 2):
        if sides[i] < sides[i + 1] + sides[i + 2]:
            return sides[i] + sides[i + 1] + sides[i + 2]
    return 0


n = int(input())
sides = list(map(int, input().split()))

result = max_triangle_perimeter(n, sides)

print(result)