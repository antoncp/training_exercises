def solution(s):
    new_s = ""
    for i in s:
        if i.isupper():
            new_s += f" {i}"
        else:
            new_s += i
    return new_s
