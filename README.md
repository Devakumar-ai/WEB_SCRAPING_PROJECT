# WEB_SCRAPING_PROJECT
# 🛒 Amazon Price Tracker & Web Scraper

A Python-based web scraping project that automatically collects **Amazon product title, price, and date** and stores the information in a CSV file. The script can run continuously and check the product price once every 24 hours.

> ⚠️ **Note:** Amazon may block automated requests or change its HTML structure. This project is intended for learning web scraping with Python and BeautifulSoup. Make sure your use complies with Amazon's terms and applicable laws.

---

## 📌 Project Overview

This project uses:

* **Python** 🐍
* **Requests** – to send HTTP requests to Amazon
* **BeautifulSoup** – to extract product information from HTML
* **CSV** – to store scraped data
* **Pandas** – to read and analyze the collected data
* **Datetime** – to record the date
* **Time** – to schedule daily scraping

The program extracts:

| Data          | Description                      |
| ------------- | -------------------------------- |
| Product Title | Apple iPhone 17 Pro Max 256 GB   |
| Price         |  1,41,000.00                     |
| Date          |  10-08-2026                      |

---

## 🚀 Features

* 🔎 Scrapes an Amazon product page
* 🏷️ Extracts the product title
* 💰 Extracts the displayed price
* 📅 Records the scraping date
* 📁 Saves results to a CSV file
* 📊 Reads the CSV using Pandas
* 🔄 Automatically checks the price every 24 hours
* 🛡️ Uses a custom User-Agent header
* 🧩 Handles missing title/price elements

---

## 🛠️ Technologies Used

```text
Python
├── requests
├── BeautifulSoup
├── csv
├── datetime
├── time
└── pandas
```

---

## 📂 Project Structure

```text
SCRAPING/
│
├── web_scraping_project.py
├── AmazonWebScraperDataSet.csv
└── README.md
```

---

## ⚙️ Installation

### 1. Install Python

Make sure Python is installed on your computer.

Check your Python version:

```bash
python --version
```

---

### 2. Install Required Libraries

Run:

```bash
pip install requests beautifulsoup4 pandas
```

---

## ▶️ How to Run

Open your project folder in VS Code or PowerShell.

For example:

```bash
cd C:\Users\hi\Desktop\SCRAPING
```

Then run:

```bash
python web_scraping_project.py
```

The program will:

1. Send a request to the Amazon product page.
2. Download the HTML.
3. Parse the HTML using BeautifulSoup.
4. Find the product title.
5. Find the product price.
6. Record today's date.
7. Save the information to the CSV file.
8. Wait 24 hours.
9. Repeat the process.

---

## 🔍 How Web Scraping Works

The basic flow of this project is:

```text
Amazon Product Page
        ↓
   requests.get()
        ↓
    HTML Response
        ↓
 BeautifulSoup Parser
        ↓
 ┌───────────────┐
 │ Product Title │
 │     Price     │
 │     Date      │
 └───────────────┘
        ↓
     CSV File
        ↓
   Pandas Analysis
```

---

## 🧑‍💻 Important Code Sections

### 1. Sending a Request

```python
response = requests.get(url, headers=headers)
```

The `requests` library sends an HTTP GET request to the Amazon product page.

The `headers` dictionary contains a browser-like User-Agent.

---

### 2. Creating BeautifulSoup Object

```python
soup2 = BeautifulSoup(response.text, "html.parser")
```

BeautifulSoup converts the HTML response into a structure that can be searched for specific elements.

---

### 3. Extracting Product Title

```python
title_tag = soup2.find(id="productTitle")

if title_tag:
    title = title_tag.get_text(strip=True)
```

The code searches for the element with:

```text
id="productTitle"
```

and extracts its text.

---

### 4. Extracting Price

```python
Price_tag = soup2.find(
    id="apex-pricetopay-accessibility-label"
)

if Price_tag:
    price = Price_tag.get_text(strip=True)
```

The code searches for the Amazon HTML element containing the displayed price.

> Amazon can change its HTML structure, so this selector may stop working in the future.

---

### 5. Getting the Current Date

```python
import datetime

today = datetime.date.today()
```

This records the date on which the price was collected.

---

### 6. Saving Data to CSV

```python
with open(
    "AmazonWebScraperDataSet.csv",
    "a+",
    newline="",
    encoding="UTF8"
) as f:
    writer = csv.writer(f)
    writer.writerow(data)
```

The `a+` mode appends new data instead of replacing existing records.

Example CSV:

```text
Title,Price,Date
Apple iPhone ...,99999,2026-08-10
Apple iPhone ...,98999,2026-08-11
Apple iPhone ...,97999,2026-08-12
```

This allows you to build a historical price dataset.

---

## 📊 Reading the Data with Pandas

The project also uses Pandas to read the CSV:

```python
import pandas as pd

df = pd.read_csv(
    r"C:\Users\hi\Desktop\SCRAPING\AmazonWebScraperDataSet.csv"
)

print(df)
```

This makes it possible to perform further analysis, such as:

* Finding the lowest price
* Finding the highest price
* Tracking price changes
* Creating price charts
* Identifying the best time to buy

---

## 🔄 Automatic Daily Price Tracking

The project uses:

```python
while True:
    check_price()
    time.sleep(86400)
```

`86400` seconds equals:

```text
60 × 60 × 24 = 86,400 seconds
```

Therefore, the script runs approximately once every **24 hours**.

---

## 📈 Possible Future Improvements

This project can be expanded into a complete **Price Alert System**.

### 🔔 1. Email Notifications

Send an email when the product price falls below a target price.

Example:

```text
Current Price: ₹89,999
Target Price: ₹90,000

🎉 Price dropped!
Send notification.
```

---

### 💾 2. Store Data in a Database

Instead of CSV, you could use:

* MySQL
* PostgreSQL
* SQLite
* MongoDB

---

### 📊 3. Create a Price History Dashboard

Use:

* Pandas
* Matplotlib
* Power BI
* Streamlit

to visualize price changes.

Example:

```text
Price
 ₹
 │
 │  ●
 │     ●
 │        ●
 │   ●
 │           ●
 └────────────────── Date
```

---

### 🌐 4. Track Multiple Products

Instead of tracking one URL:

```python
products = [
    "product_url_1",
    "product_url_2",
    "product_url_3"
]
```

The program could monitor multiple products.

---

### ⚡ 5. Add a Price Alert

For example:

```python
if price < 90000:
    send_email()
```

This would automatically notify you when the price reaches your target.

---

## 🐛 Common Problems

### `AttributeError: 'NoneType' object has no attribute 'get_text'`

This usually means BeautifulSoup couldn't find the requested HTML element.

For example:

```python
soup.find(id="productTitle")
```

returned `None`.

Use:

```python
title_tag = soup.find(id="productTitle")

if title_tag:
    title = title_tag.get_text(strip=True)
else:
    print("Product title not found")
```

Possible reasons include:

* Amazon changed its HTML
* Amazon returned a different page
* Request was blocked
* Product page requires additional verification
* Incorrect URL

---

### `PermissionError: [Errno 13] Permission denied`

This can happen when:

* The CSV is open in Excel
* Another program is using the file
* You don't have permission to modify the directory

Close the CSV file before running the script again.

---

## ⚠️ Important Improvement to Your Current Code

Your current script first creates the CSV using:

```python
'w'
```

and then appends to it using:

```python
'a+'
```

The `w` mode **overwrites the existing CSV every time the program starts**.

For a price tracker, you normally want to create the header only if the file doesn't already exist.

A better approach is:

```python
import os
import csv

file_name = "AmazonWebScraperDataSet.csv"

file_exists = os.path.exists(file_name)

with open(
    file_name,
    "a",
    newline="",
    encoding="UTF8"
) as f:

    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["Title", "Price", "Date"])

    writer.writerow([title, price, today])
```

This preserves your historical price data.

---

## 🎯 Learning Outcomes

By completing this project, you practice:

* Python programming
* HTTP requests
* Web scraping
* HTML parsing
* BeautifulSoup
* CSV file handling
* Pandas
* Exception/error handling
* Automation with loops and delays
* Basic data collection pipelines

---

## 🚀 Future Project Goal

The ultimate version of this project could become:

```text
Amazon
   ↓
Web Scraper
   ↓
Price Extraction
   ↓
Database
   ↓
Price History
   ↓
Price Analysis
   ↓
Target Price Check
   ↓
📧 Email / 📱 Notification
   ↓
User
```

This would turn the current scraper into a complete **automated Amazon Price Tracking & Alert System**.

---

## 👨‍💻 Author

**Deva Dev**

This project was created as a Python web-scraping and automation learning project.

---

## ⭐ If You Like This Project

You can improve it by adding:

* Multiple product tracking
* Email alerts
* Telegram notifications
* Price-history graphs
* SQLite/MySQL database
* Streamlit dashboard
* Scheduled execution
* Error logging
* Automatic retry handling

