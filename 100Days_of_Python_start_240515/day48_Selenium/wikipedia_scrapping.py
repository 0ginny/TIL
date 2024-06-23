from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

search_url = 'https://en.wikipedia.org/wiki/Main_Page'

driver = webdriver.Chrome(options=chrome_options)
driver.get(search_url)

num_articles = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]').text
print(num_articles)


driver.quit()