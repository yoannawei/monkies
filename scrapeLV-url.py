from bs4 import BeautifulSoup

import requests
import re
import pprint

url = "https://us.louisvuitton.com/eng-us/women/handbags/all-handbags/_/N-mzlp5k/to-18"

lv_data = requests.get(url).text

lv_soup = BeautifulSoup(lv_data, "lxml")

# get product tnames

product_tags = lv_soup.find_all("div", "productName")
product_names = []
for tag in product_tags:
    product_names.append(tag.contents[0])

#print(product_names)

# retrieve product prices
# product_price_tags = lv_soup.find_all(attrs={"class" : "productPrice notCrawlableContent"})
product_price_tags = lv_soup.find_all("div", "productPrice")
product_prices = []
for tag in product_price_tags:
   product_price = tag.attrs['data-htmlcontent']
   product_prices.append(product_price)
#print(product_prices)

price_list = dict(zip(product_names, product_prices))

for key in price_list:
    print(key+': '+price_list[key])
