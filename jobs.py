import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    url = "https://remoteok.com/remote-dev-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}

    jobs = []

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        listings = soup.find_all("tr", class_="job")

        for job in listings[:10]:
            title = job.find("h2")
            company = job.find("h3")
            link = job.get("data-href")

            jobs.append({
                "category": "job",
                "title": title.text if title else "N/A",
                "company": company.text if company else "N/A",
                "location": "Remote",
                "link": "https://remoteok.com" + link if link else "N/A"
            })

    except Exception as e:
        print("Error scraping jobs:", e)

    return jobs