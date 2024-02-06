def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def total(arr):
    res = [i for x, i in enumerate(arr) if is_prime(x)]
    return sum(res)
