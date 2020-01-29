import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Powerbeats-Pro-Totally-Wireless-Earphones/dp/B07W5JZBVJ?pf_rd_p=d22f02ec-561d-470e-9f56-891084a0600d&pd_rd_wg=25BcG&pf_rd_r=3DE1YHRQPZF1GBFJDBDP&ref_=pd_gw_unk&pd_rd_w=dJ6Or&pd_rd_r=0c9cf858-2a70-4805-b6b0-754f40ed287d'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
}

def check_price():
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	converted_price = float(price[0:5])
	if(converted_price < 1000.50):
    	send_mail()

	print(converted_price)
	print(title.strip())

def	send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	