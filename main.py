from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# #Scraping the price from the website

response = requests.get(f"https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
data = response.text
soup = BeautifulSoup(data, "html.parser")
list = soup.find_all(class_="a-price-whole")
price = list[1].text
price = int(price.replace(".", ""))

# #Sending the e-mail

if price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.getenv("my_email"), password=os.getenv("password"))
        connection.sendmail(
            from_addr=os.getenv("my_email"),
            to_addrs=os.getenv("sender"),
            msg=f"Subject:Amazon price alert!!\n\n{f"Your awaited amazon product has come down below the target price for {price}"}")
