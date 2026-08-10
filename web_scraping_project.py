# import libraries 
import requests
from bs4 import BeautifulSoup
import time
#import smtplib use this to send email when it statifies the condtion 

# Connect to Website and pull in data
url = "https://www.amazon.in/iPhone-Pro-Max-256-Promotion/dp/B0FQFW4MVJ/?_encoding=UTF8&pd_rd_w=GVaSk&content-id=amzn1.sym.bf12f591-ec9a-43db-a9f6-c4d4b79453f7&pf_rd_p=bf12f591-ec9a-43db-a9f6-c4d4b79453f7&pf_rd_r=DSY05WV8322A611A9T88&pd_rd_wg=HSu6y&pd_rd_r=ff413270-a7ad-4327-8ede-01c482470d9f&ref_=pd_hp_d_atf_dealz_m1&th=1"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.url)
print(response.text[:1000])

soup2 = BeautifulSoup(response.text, "html.parser")
#------------------------------------------------
#Finding of title 
#------------------------------------------------
title_tag = soup2.find(id="productTitle")

if title_tag:
    title = title_tag.get_text(strip=True)
    title=title.strip()# Stripe is used for standardizing the title
    print(title)
else:
    print("productTitle was not found")

#------------------------------------------------
#Finding of Price_tag
#------------------------------------------------
Price_tag=soup2.find(id='apex-pricetopay-accessibility-label')

if Price_tag:
    price=Price_tag.get_text(strip=True)
    price=price.strip()[1:12] # Stripe is used for standardizing the price_tag 
    print(price)
else:
    print("price tag not found")


# Create a Timestamp for your output to track when data was collected
import datetime

today=datetime.date.today()
#print(today)

#TCreate CSV and write headers and data into the file 
import csv

headers=['Title','Price','Date']
data = [title,price,today]

with open("AmazonWebScraperDataSet.csv",'w',newline='',encoding='UTF8') as f:
    writer=csv.writer(f)
    writer.writerow(headers)
    writer.writerow(data)


#Now we are appending the data to the csv

with open("AmazonWebScraperDataSet.csv",'a+',newline='',encoding='UTF8') as f:
    writer=csv.writer(f)
    writer.writerow(data)

#to read data
import pandas as pd

df=pd.read_csv(r'C:\Users\hi\Desktop\SCRAPING\AmazonWebScraperDataSet.csv')
print(df)

#Combine all of the above code into one function

def check_price():

    url = "https://www.amazon.in/iPhone-Pro-Max-256-Promotion/dp/B0FQFW4MVJ/?_encoding=UTF8&pd_rd_w=GVaSk&content-id=amzn1.sym.bf12f591-ec9a-43db-a9f6-c4d4b79453f7&pf_rd_p=bf12f591-ec9a-43db-a9f6-c4d4b79453f7&pf_rd_r=DSY05WV8322A611A9T88&pd_rd_wg=HSu6y&pd_rd_r=ff413270-a7ad-4327-8ede-01c482470d9f&ref_=pd_hp_d_atf_dealz_m1&th=1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup2 = BeautifulSoup(response.text, "html.parser")

    title_tag = soup2.find(id="productTitle")
    if title_tag:
        title = title_tag.get_text(strip=True)
        title=title.strip()# used strip for better view
        print(title)
    else:
        print("productTitle was not found")

    Price_tag=soup2.find(id='apex-pricetopay-accessibility-label')

    if Price_tag:
        price=Price_tag.get_text(strip=True)
        price=price.strip()[1:12] #used strip for better view
        print(price)
    else:
        print("price tag not found")

    import datetime
    today=datetime.date.today()

    import csv
    headers=['Title','Price','Date']
    data = [title,price,today]

    with open("AmazonWebScraperDataSet.csv",'a+',newline='',encoding='UTF8') as f:
        writer=csv.writer(f)
        writer.writerow(data)

#Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400) 
# it checks daily as 60sec*60min*24hrs=864000sec



























