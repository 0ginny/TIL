from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# chrome driver download
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.speedtest.net/"

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach',True)
# headless mode
# 윈도우 사이즈가 없으면 click에러가 생김. window가 작을 때 element가 생성되지 않을 수 있나봐
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
# 로딩 대기시간 sec

# WebDriverWait doc :
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
wait = WebDriverWait(driver, 60)

btn_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]'
down_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
upload_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'

# 속도검사 시작
# 버튼이 클릭 가능할 때까지 wait
wait.until(EC.element_to_be_clickable((By.XPATH, btn_xpath)))
start_btn = driver.find_element(by=By.XPATH, value=btn_xpath)
start_btn.click()
print('click')
# 검사결과 출력
# 결과가 나오면 반드시 소숫점이 생기는 것을 이용한 로딩 wait
wait.until(EC.text_to_be_present_in_element((By.XPATH, down_xpath), '.'))
down_speed = driver.find_element(By.XPATH, down_xpath)
print(f'download speed : {down_speed.text} Mbps')

wait.until(EC.text_to_be_present_in_element((By.XPATH, upload_xpath), '.'))
upload_speed = driver.find_element(By.XPATH, upload_xpath)
print(f'upload speed : {upload_speed.text} Mbps')

