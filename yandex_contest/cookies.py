num_kids = int(input())
kids = list(map(int, input().split()))
num_cook = int(input())
cookies = sorted(list(map(int, input().split())), reverse=True)

lucky_kids = 0

for kid in sorted(kids, reverse=True):
    if cookies and kid <= cookies[0]:
        cookies.pop(0)
        lucky_kids += 1

print(lucky_kids)
