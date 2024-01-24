import re


def calculate(s):
    first = ""
    for i in s:
        if i.isdigit():
            first += i
        else:
            break
    plus = re.findall(r"plus[0-9]+", s)
    minus = re.findall(r"minus[0-9]+", s)
    plus = [re.sub(r"plus", "", i) for i in plus]
    minus = [re.sub(r"minus", "", i) for i in minus]
    return str(int(first) + sum(map(int, plus)) - sum(map(int, minus)))
