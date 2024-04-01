from re import search

import requests


def get_honor(username):
    user_page = requests.get(f"https://www.codewars.com/users/{username}")
    if user_page.status_code == 200:
        span = search(
            r'<div class="stat"><b>Honor:</b>(.*?)</div>', user_page.text
        )
        return int(span.group(1).replace(",", ""))
    raise ValueError
