nums = [int(x) % 2 for x in input().split()]
print('WIN' if all(nums) or not any(nums) else 'FAIL')
