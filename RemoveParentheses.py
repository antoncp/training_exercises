def remove_parentheses(s):
    result = []
    exclude = 0
    for i in s:
        if i == "(":
            exclude += 1
        elif i == ")":
            exclude -= 1
            continue
        if exclude != 0:
            continue
        result.append(i)
    return "".join(result)
