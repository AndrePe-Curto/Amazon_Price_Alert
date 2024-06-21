from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import os
import smtplib
from fake_useragent import UserAgent

# Function to get soup with retry mechanism and fake user agent
def get_soup_retry(url):
    ua = UserAgent()
    uag_random = ua.random

    header = {
        'User-Agent': uag_random,
        'Accept-Language': 'en-US,en;q=0.9'
    }
    isCaptcha = True
    while isCaptcha:
        page = requests.get(url, headers=header)
        assert page.status_code == 200
        soup = BeautifulSoup(page.content, 'lxml')
        if 'captcha' in str(soup):
            uag_random = ua.random
            print(f'\rBot has been detected... retrying ... use new identity: {uag_random} ', end='', flush=True)
            continue
        else:
            print('Bot bypassed')
            return soup


# Connect to Website and get price
def check_price():
    URL = 'https://www.amazon.es/-/pt/dp/B0CGVSLM1C/'
    
    soup = get_soup_retry(URL)

    title = soup.find(id='productTitle').get_text()
    title = title.strip()

    price = soup.find(class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay').get_text()
    price = price.replace('\n', '').replace(' ', '').replace('€', '').replace(',', '.').replace('\xa0', '')
    price = float(price)

    return title, price


def date_price():
    today = datetime.datetime.now()
    date = today.strftime("%d/%m/%Y %H:%M")
    return date


def write_csv(title, price, date):
    file_exists = os.path.isfile('AmazonPrice.csv')
    with open('AmazonPrice.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        header = ['Title', 'Price', 'Date']
        data = [title, price, date]
        
        if not file_exists:
            writer.writerow(header)
        
        writer.writerow(data)

#To use Gmail as your email sender, you’ll need to enable app passwords. 
#Explanation in link bellow
#https://support.google.com/mail/answer/185833?hl=en
'''
def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('your_email@gmail.com', 'your_password')
    
    subject = "Google Pixel 8 Pro 512 GB is below 1050€"
    body = ("André, This is the moment we have been waiting for. Now is your chance to pick up the phone of your dreams. "
            "Don't mess it up! Link here: https://www.amazon.es/-/pt/dp/B0CGVSLM1C/")
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'your_email@gmail.com'  # Sender
        'recipient@gmail.com',  # Recipient
        msg.encode('utf-8')  # Encode the message in utf-8
    )
    server.quit()
'''

while(True):
    title, price = check_price()
    date = date_price()
    write_csv(title, price, date)
    #if price < 1050:
        #print("Email sent")
        #send_mail()
    time.sleep(86400)  # Sleep for 1 day
