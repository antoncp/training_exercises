def longest_palindrome(s):
    s = s.lower()
    size = 0
    addition = 0
    for i in set(s):
        if i.isalnum():
            replays = s.count(i)
            if replays > 1:
                if replays % 2 == 0:
                    size += replays
                else:
                    size += (replays // 2) * 2
                    addition = 1
            else:
                addition = 1
    return size + addition
