import requests
import bs4
import smtplib

MY_EMAIL = "engtesting23@gmail.com"
PASSWORD = "**********"

URL = "https://www.amazon.in/Eastfield-Allround-Professional-Tennis-Racquet/dp/B01M037GDB/ref=sr_1_5?crid=2P5V3JDLKZBZ&keywords=Eastfield+Allround+Professional+Table+Tennis+Racket&qid=1688104663&sprefix=eastfield+allround+professional+table+tennis+racket%2Caps%2C227&sr=8-5"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url=URL, headers=headers)

soup = bs4.BeautifulSoup(response.text, "lxml")
string_price = soup.find(name="span", class_="a-price-whole").getText()
split_price1 = string_price.split(",")[0]
split_price2 = string_price.split(",")[1]
amazon_price = float(split_price1 + split_price2)

if amazon_price < 5500:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="engtechno25@gmail.com",
            msg=f"Subject:Minimum amazon price alert\n"
                "Eastfield Allround Professional Wooden Table Tennis Racquet is now available at less than Rs.5500/-\n"
                "Please go to given link and purchase it asap.\n"
                f"Product Link- {URL}\nThank You!"
        )

