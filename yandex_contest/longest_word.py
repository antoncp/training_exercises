text_length = input()
words = input().split()
longest, length = None, 0
for i in words:
    if len(i) > length:
        longest, length = i, len(i)
print(longest)
print(length)
