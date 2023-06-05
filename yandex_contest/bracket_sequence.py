def is_correct_bracket_seq(string):
    all = []
    par = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    for i in string:
        if i in ['(', '[', '{']:
            all.append(i)
        else:
            if all and all[-1] == par[i]:
                all.pop()
            else:
                return False
    return True if not all else False


print(is_correct_bracket_seq(input()))
