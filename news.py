import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = "https://news.ycombinator.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    news_list = []

    try:
        response = requests.get(url, headers=headers)

        print("Status Code:", response.status_code)

        if response.status_code != 200:
            print("Failed to fetch website!")
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        posts = soup.select("span.titleline > a")

        print("Posts found:", len(posts))

        for post in posts[:10]:
            title = post.text.strip()
            link = post.get("href")

            if title and link.startswith("http"):
                news_list.append({
                    "category": "news",
                    "title": title,
                    "link": link
                })

    except Exception as e:
        print("Error scraping news:", e)

    return news_list