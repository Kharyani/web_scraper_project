from scraper.jobs import scrape_jobs
from scraper.products import scrape_products
from scraper.news import scrape_news
from utils.storage import save_json, save_csv
from utils.search_filter import search_data

data = []

def menu():
    while True:
        print("\n===== WEB SCRAPER MENU =====")
        print("1. Scrape Jobs")
        print("2. Scrape Products")
        print("3. Scrape News")
        print("4. Search Data")
        print("5. Save Data")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            jobs = scrape_jobs()
            data.extend(jobs)
            print("\n--- Jobs Scraped ---")
            for job in jobs:
                print(job)

        elif choice == "2":
            products = scrape_products()
            data.extend(products)
            print("\n--- Products Scraped ---")
            for product in products:
                print(product)

        elif choice == "3":
            news = scrape_news()
            data.extend(news)
            print("\n--- News Scraped ---")
            for item in news:
                print(item)

        elif choice == "4":
            keyword = input("Enter keyword: ")
            search_data(data, keyword)

        elif choice == "5":
            save_json(data)
            save_csv(data)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

menu()