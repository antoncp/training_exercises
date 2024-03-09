def one_two_three(n):
    if n == 0:
        return [0, 0]
    base = "9" * x if (x := n // 9) > 0 else ""
    base_rest = str(y) if (y := n % 9) != 0 else ""
    rest = int("1" * n)
    return [int(base + base_rest), rest]
