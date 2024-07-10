def ips_between(start, end):
    start = sum(int(i)*(256**num) for num, i in enumerate(reversed(start.split('.'))))
    end = sum(int(i)*(256**num) for num, i in enumerate(reversed(end.split('.'))))
    return end-start
