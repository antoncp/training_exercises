def fibonacci_last_k_digits(n, k):
    ab = [1, 1]
    d = (10 ** k)
    if n < 2:
        fib = 1
    else:
        n -= 1
        for i in range(n):
            s = (ab[0] + ab[1]) % d
            ab[0] = ab[1]
            ab[1] = s
        fib = ab[1]
    return fib


n, k = map(int, input().split())
result = fibonacci_last_k_digits(n, k)
print(result)
