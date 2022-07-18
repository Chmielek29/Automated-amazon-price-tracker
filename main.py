import requests
from bs4 import BeautifulSoup
import smtplib

my_email = 
password = 

URL = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/?_encoding=UTF8&pd_rd_w=eUhUs&pf_rd_p=716a1ed9-074f-4780-9325-0019fece3c64&pf_rd_r=XACSC8MRFVBT4RXC1MN8&pd_rd_r=f1e97c34-c40a-4bd8-9caa-5b7edf52410f&pd_rd_wg=LdWKz&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"
UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72"
Language = "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"

response = requests.get(URL, headers={"User-Agent":UserAgent, "Accept-Language":Language})
soup = BeautifulSoup(response.content, 'lxml')

price = soup.find("span", class_="a-offscreen")
price_float = float(price.getText().split("$")[1])
print(price_float)

product = soup.find("span", id="productTitle").getText()
print(product)

message = f"{product} is now ${price_float}"

if price_float < 200:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=address,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8"))
