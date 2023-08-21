def check_logs(log):
    if log:
        days = 1
    else:
        days = 0
    for x, i in enumerate(log[1:], start=1):
        if (
            int(i.replace(":", "")) < int(log[x - 1].replace(":", ""))
            or i == log[x - 1]
        ):
            days += 1
    return days
