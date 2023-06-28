num_houses, budget = map(int, input().split())
all_houses = sorted(list(map(int, input().split())), reverse=True)

purchases = 0

while budget > 0 and all_houses:
    budget -= all_houses.pop()
    purchases += 1

if budget >= 0:
    print(purchases)
else:
    print(purchases-1)
