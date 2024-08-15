import heapq


def queue_time(customers, n):
    if not customers:
        return 0
    tills = [0] * n
    for i in customers:
        heapq.heapreplace(tills, tills[0]+i)
    return max(tills)
