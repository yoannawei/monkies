from __future__ import division, unicode_literals
import codecs
from bs4 import BeautifulSoup


lv_html = codecs.open("LV.html", "r")
lv_doc = lv_html.read()

lv_soup = BeautifulSoup(lv_doc, "lxml")

# get product names
product_tags = lv_soup.find_all("div", "productName")
product_names = []
for tag in product_tags:
    product_names.append(tag.contents[0])

print(product_names)

# retrieve product prices
product_price_tags = lv_soup.find_all(attrs={"class" : "productPrice notCrawlableContent"})

product_prices = []
for tag in product_price_tags:
   product_price = tag.attrs['data-htmlcontent']
   product_prices.append(product_price)

print(product_prices)
new_dict = dict(zip(product_names, product_prices))

print(new_dict)

