import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def open_browser():
#Run on Chrome browser
#chrome = webdriver.Chrome("C:\Program Files\ChromeDriver\chromedriver.exe")
#chrome.get("https://us.louisvuitton.com/eng-us/women/handbags/all-handbags/_/N-mzlp5k")

# Run on Firefox
    firefox = webdriver.Firefox("C:\Program Files\GeckoDriver")
    firefox.get("https://us.louisvuitton.com/eng-us/women/handbags/all-handbags/_/N-mzlp5k")

    time.sleep(1)

    elem = firefox.find_element_by_tag_name("body")

    no_of_pagedowns = 10

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1

    # Get product names
    products_names = firefox.find_elements_by_class_name("product-item tagClick tagClick")
    
    print(products_names)
        


if __name__ == "__main__":
    open_browser()



