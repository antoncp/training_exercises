def calc(x):
    total1 = "".join([str(ord(i)) for i in x])
    total2 = str(total1.replace("7", "1"))
    return sum(map(int, list(total1))) - sum(map(int, list(total2)))
