import requests
from bs4 import BeautifulSoup

base_url = "https://www.scrapethissite.com"
url = requests.get("https://www.scrapethissite.com/pages/").text
soup = BeautifulSoup(url, "lxml")

for article in soup.find_all("div", class_="page"):
    try:
        heading = article.find("h3", class_="page-title").text.strip()
        print(heading)
    except AttributeError:
        print("Heading not found")

    try:
        summary = article.find("p", class_="lead session-desc").text.strip()
        print(summary)
    except AttributeError:
        print("Summary not found")

    try:
        link = article.a.get("href")
        full_link = base_url + link
        print(full_link)
    except AttributeError:
        print("Link not found")

    print()
