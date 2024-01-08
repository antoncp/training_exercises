def add(n):
    def add_another(y):
        return y+n
    return add_another
