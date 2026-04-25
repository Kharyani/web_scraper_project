import requests
from bs4 import BeautifulSoup

def scrape_products():
    url = "https://books.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    products = []

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books[:10]:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.encode('utf-8').decode('utf-8')
            price = price.replace('Â', '')

            products.append({
                "category": "product",
                "name": title,
                "price": price,
                "rating": "N/A",
                "link": url
            })

    except Exception as e:
        print("Error scraping products:", e)

    return products