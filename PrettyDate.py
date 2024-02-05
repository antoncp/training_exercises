def to_pretty(seconds):
    vars = [
        [0, 604800, "weeks ago", "a week ago"],
        [0, 86400, "days ago", "a day ago"],
        [0, 3600, "hours ago", "an hour ago"],
        [0, 60, "minutes ago", "a minute ago"],
        [0, 1, "seconds ago", "a second ago"],
    ]
    if seconds == 0:
        return "just now"
    for var in vars:
        var[0] = seconds // var[1]
    for var in vars:
        if var[0]:
            if var[0] == 1:
                return var[3]
            return f"{var[0]} {var[2]}"
