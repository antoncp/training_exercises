def format_duration(seconds):
    if seconds == 0:
        return 'now'
    times = {
        'min': (60, 'minute', 'minutes'),
        'hour': (3600, 'hour', 'hours'),
        'day': (86400, 'day', 'days'),
        'year': (31536000, 'year', 'years'),
    }

    result = []

    for time in reversed(times):
        quantity = seconds//times[time][0]
        if quantity:
            if quantity == 1:
                result.append(f'{quantity} {times[time][1]}')
            else:
                result.append(f'{quantity} {times[time][2]}')
            seconds -= quantity * times[time][0]

    if seconds:
        if seconds == 1:
            result.append('1 second')
        else:
            result.append(f'{seconds} seconds')

    return (', '.join(result[:-1]) + f' and {result[-1]}' if len(result) > 1
            else str(*result))
