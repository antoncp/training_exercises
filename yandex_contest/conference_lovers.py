n = int(input())
students = input().split()
limit = int(input()) 
final = {}
for i in students:
    final[i] = final.get(i, 0) + 1
sor_dict = dict(sorted(final.items(), key=lambda i: i[1], reverse=True))
print(*list(sor_dict.keys())[:limit])