from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--headless')
search_url = "https://www.python.org/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=search_url)

# '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]'
# '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time'
# '//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[1]/a'
# '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]'
# print(div_tag.text.split('\n'))
ul_tag = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
li_tags = ul_tag.find_elements(by=By.TAG_NAME,value='li')

news_dict = {}
for idx,li_tag in enumerate(li_tags):
    time, name = li_tag.text.split('\n')
    news_dict[idx] = {'time': time,
                      'name': name}

print(news_dict)

driver.quit()
