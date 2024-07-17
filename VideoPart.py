import math


def video_part(part, total):
    part = sum(int(i)*(60**n) for n, i in enumerate(part.split(':')[::-1]))
    total = sum(int(i)*(60**n) for n, i in enumerate(total.split(':')[::-1]))
    gcd = math.gcd(part, total)
    return [part//gcd, total//gcd]
