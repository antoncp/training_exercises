def solution(s):
    new_order = ""
    for i in s:
        if i.isupper():
            new_order += f" {i}"
        else:
            new_order += i
    return new_order
