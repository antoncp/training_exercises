def eliminate_unset_bits(number):
    num = "".join(i for i in number if i != "0")
    if not num:
        return 0
    return int(num, 2)
