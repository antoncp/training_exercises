import requests
from bs4 import BeautifulSoup


def get_honor(username):
    user_page = requests.get(f"https://www.codewars.com/users/{username}")
    if user_page.status_code == 200:
        soup = BeautifulSoup(user_page.content, "html.parser")
        honor = soup.select(
            "#shell_content > div.w-256.max-w-full.mx-auto.mb-0.mt-4.p-0 > div > div > div:nth-child(1) > div > section > div.stat-container > div > div:nth-child(1) > div:nth-child(2)"
        )
        if honor:
            return int(honor[0].text.split(":")[1].replace(",", ""))
        honor = soup.select(
            "#shell_content > div.w-256.max-w-full.mx-auto.mb-0.mt-4.p-0 > div > div > div:nth-child(2) > div > section > div.stat-container > div > div:nth-child(1) > div:nth-child(2)"
        )
        if honor:
            return int(honor[0].text.split(":")[1].replace(",", ""))
    raise ValueError
