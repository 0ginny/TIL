from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



stop_sec = 60

url = 'https://orteil.dashnet.org/experiments/cookie/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
money = driver.find_element(By.XPATH, '//*[@id="money"]')
store = driver.find_element(By.XPATH, '//*[@id="store"]')

store_dict = {}
products = store.find_elements(By.TAG_NAME, 'div')
for product in products:
    menu = product.find_element(By.TAG_NAME, 'b').text.strip()
    if menu != '':  # 공백 제외
        name, price = menu.split(' - ')
        store_dict[name] = int(price.replace(',', ''))
# print(list(store_dict.keys())[::-1])


def click_cookie(interber=0.01):
    try:
        cookie.click()
        time.sleep(interber)
    except Exception:
        pass


def buy(name, interber=20):
    try :
        buy_product = driver.find_element(By.ID, f'buy{name}')
        buy_product.click()
        # 가격 조정
        # WebDriverWait(driver, interber).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, f'div#buy{name} b')))
        menu = buy_product.find_element(By.TAG_NAME, 'b')
        price = menu.text.split(' - ')[-1]
        store_dict[name] = int(price.replace(',', ''))
    except Exception:
        print('error exist')



def get_total_money(interber=10):
    global money
    # WebDriverWait(driver, interber).until(EC.presence_of_all_elements_located((By.ID, 'money')))
    try :
        money = driver.find_element(By.ID, 'money')
    except Exception:
        pass

# main roop
start_sec = time.time()
while time.time()-start_sec < stop_sec :
    click_cookie()
    for name in list(store_dict.keys())[::-1]:
        if int(money.text) >= store_dict[name]:
            buy(name)
            get_total_money()
    get_total_money()

# 초당 생산량 출력
income_per_sec = driver.find_element(By.ID,'cps')
print(income_per_sec.text)