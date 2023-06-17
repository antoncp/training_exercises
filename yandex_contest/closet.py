n = int(input())
closet = input().split()
final = {}
for i in closet:
    final[i] = final.get(i, 0) + 1
print("".join(f"{k} "*v for k, v in sorted(final.items())))
