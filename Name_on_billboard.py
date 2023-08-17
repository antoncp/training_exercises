def billboard(name, price=30):
    total = 0
    for i in name:
        total += price
    return total
