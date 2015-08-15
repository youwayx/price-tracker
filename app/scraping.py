from lxml import html
import datetime
import requests

reqpage = 'http://www.amazon.com/dp/B00GDQ0RMG/ref=ods_gw_d_L_h1_montoya?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=desktop-hero-kindle-A&pf_rd_r=0V99RYRC7YNKQGV04JGZ&pf_rd_t=36701&pf_rd_p=2133728942&pf_rd_i=desktop'
pg1 = 'http://www.amazon.com/Anker-Generation-Astro-mini-Lipstick-Sized/dp/B005X1Y7I2/ref=zg_bs_7073960011_1'

def get_amazon_price(website):
	page = requests.get(website)
	tree = html.fromstring(page.text)
	d = datetime.datetime.now()
	try:
		price = tree.xpath('//*[@id="priceblock_ourprice"]/text()')

		if len(price)==0:
			price = tree.xpath('//*[@id="priceblock_saleprice"]/text()')

		p = int(float(price[0][1:])*100)
		return {"success": True, "url":website, "price":p, "time":d.isoformat()}
	except:
		return {"success": False, "message": "No price found"}
