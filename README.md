# 🕸️ Dynamic Web Scraper (Jobs / Products / News)

## 📌 Project Overview

This project is a **Python-based CLI (Command Line Interface) Web Scraper** that extracts real-time data from different websites including **jobs, products, and news**.

It simulates real-world data collection systems used in industries for gathering structured information from web sources.

---

## 🎯 Features

### 🔹 Web Scraping

* Scrapes data from multiple websites:

  * Jobs (Remote listings)
  * Products (Books)
  * News (Tech news headlines)
* Uses:

  * `requests`
  * `BeautifulSoup`

---

### 🔹 Data Extraction

Extracted fields include:

#### 🧑‍💼 Jobs:

* Job Title
* Company
* Location
* Apply Link

#### 🛒 Products:

* Product Name
* Price
* Rating
* Product Link

#### 📰 News:

* Title
* Source Link

---

### 🔹 Search & Filter

* Search scraped data using keywords
* Works across all categories

---

### 🔹 Data Storage

* Save extracted data into:

  * JSON file (`data.json`)
  * CSV file (`data.csv`)

---

### 🔹 Menu System

Interactive CLI menu:

1. Scrape Jobs
2. Scrape Products
3. Scrape News
4. Search Data
5. Save Data
6. Exit

---

## ⚙️ Technologies Used

* Python 3
* Requests
* BeautifulSoup4
* Pandas

---

## 📁 Project Structure

```
web_scraper_project/
│── main.py
│── scraper/
│   │── jobs.py
│   │── products.py
│   │── news.py
│── utils/
│   │── storage.py
│   │── search_filter.py
│── data/
│   │── data.json
│   │── data.csv
│── README.md
```

---

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your system.

---

### Step 2: Install Required Libraries

Run the following command:

```
pip install requests beautifulsoup4 pandas
```

*(If pip doesn’t work, use: `python -m pip install ...`)*

---

### Step 3: Run the Application

```
python main.py
```

---

## 🌐 Websites Used

* https://remoteok.com (Jobs)
* https://books.toscrape.com (Products)
* https://news.ycombinator.com (News)

---

## ⚠️ Error Handling

* Handles request failures
* Uses headers to prevent blocking
* Avoids invalid or duplicate data

---

## ⭐ Advanced Features

* Modular code structure
* Clean data extraction
* Basic filtering system

---

## 📸 Screenshots (To Include)

* Menu interface
* Scraped products output
* Scraped news output
* Search results
* JSON file
* CSV file

---

## 🎥 Demo Video

A short demo video (1–2 minutes) showing:

* Menu navigation
* Scraping data
* Searching data
* Saving data

---

## 📦 Deliverables

* Source Code (ZIP)
* Sample JSON/CSV files
* Screenshots
* GitHub Repository
* README.md
* Demo Video

---

## 👨‍💻 Author

Kashish Haryani

---

## 📌 Conclusion

This project demonstrates how web scraping can be used to collect, process, and store real-time data efficiently using Python. It reflects real-world applications in data engineering and automation systems.

---
