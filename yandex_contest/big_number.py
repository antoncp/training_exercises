n = int(input())
nums = input().split()
result = sorted(nums, key=lambda x: x * 3, reverse=True)
print("".join(result))
