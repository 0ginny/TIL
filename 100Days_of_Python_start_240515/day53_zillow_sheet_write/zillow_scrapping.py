from bs4 import BeautifulSoup
import requests
from selenium import webdriver
# from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.91741408300781%2C%22east%22%3A-121.94924391699219%2C%22south%22%3A37.447296896720076%2C%22north%22%3A38.10183729678782%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
#-----------------------------
# beautifulsoup는 작동이 안됨.

# zillow cite
# 자동 입력 방지를 못 뚫음... 잘 되다가 안되다가 함. 연속해서 하면 안될 듯.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
# 헤드레스는 작동 안됨.
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
wait = WebDriverWait(driver, 30)

# list xpath
'//*[@id="grid-search-results"]/ul'
list_css = 'div.property-card-data'
# price xpath
span_data_test = 'property-card-data'

# address
address_css = 'a.property-card-link'

'//*[@id="zpid_2054930438"]/div/div[1]'
'//*[@id="zpid_2054930438"]/div/div[1]/a'
'//*[@id="zpid_2054930438"]/div/div[1]/a/address'
'//*[@id="zpid_2054930438"]/div/div[1]/div[2]/div/span'


'//*[@id="zpid_37.867622--122.25865"]/div/div[1]'

'//*[@id="zpid_37.86855--122.258766"]/div/div[1]'
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, list_css)))
house_list = driver.find_elements(By.CSS_SELECTOR, list_css)
links = []
addresses= []
prices = []
for house in house_list:
    links.append(house.find_element(By.XPATH,'/a').get_attribute('href'))
    addresses.append(house.find_element(By.XPATH,'/a/address').text)
    prices.append(house.find_element(By.XPATH,'/div[2]/div/span'))

print('links')
print(links)

print('addresses')
print(addresses)

print('prices')
print(prices)

data = {
    "address" : addresses,
    "price" : prices,
    "link" : links
}

pd_data = pd.DataFrame(data,index=None)
pd_data.to_csv("zillow_prices")


# driver.close()

#--------------------------

# # beautiful soup로 작동
# from bs4 import BeautifulSoup
# import requests
# import urllib.request as req
#
#
# # response = requests.get(url,verify=False)
# response = req.urlopen(url)
# print(response)
