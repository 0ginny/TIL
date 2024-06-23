from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://secure-retreat-92358.herokuapp.com/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

first_name_input = driver.find_element(by=By.XPATH,value='/html/body/form/input[1]')
first_name_input.send_keys("young")

last_name_input = driver.find_element(by=By.XPATH,value='/html/body/form/input[2]')
last_name_input.send_keys('ginny')

email_input = driver.find_element(by=By.XPATH,value='/html/body/form/input[3]')
email_input.send_keys('yginny@abc.com')

sign_up_btn = driver.find_element(by=By.XPATH,value='/html/body/form/button')
sign_up_btn.click()