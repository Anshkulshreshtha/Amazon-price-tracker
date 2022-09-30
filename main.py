#  this code is creating errrors because my gmail account is protected to unauthrized third party services like python
# if u want your gmail the watch lacture on how to unprotected gmail account.

import requests
import smtplib
from bs4 import BeautifulSoup

my_email = "--------------@gmail.com"
my_password = "**************"

url = "https://www.amazon.in/SanDisk-Ultra-064G-I35-SDCZ48-Drive/dp/B00KYK2ABI/ref=sr_1_7?keywords=pendrive&" \
      "qid=1657825177&refinements=p_n_size_browse-bin%3A1464338031&rnid=1464332031&s=computers&sr=1-7 "

headers = {
    "Accept_Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  "(KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

Soup = BeautifulSoup(response.text, "html.parser")
Price = Soup.find("span", class_="a-price-whole")
floating_price = float(Price.getText())

if floating_price < 700.00:
    message = "Hello Ansh, your waiting is now comes to end. as your product SANDISK-PENDRIVE comes to lowest price/n"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="anshkulshreshtha01@gmail.com",
        msg=f"subject:AMAZON-PRICE-ALERT!\n\n{message}\n{url}"
    )
