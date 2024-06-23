from selenium import webdriver
from selenium.webdriver.common.by import By

# to keep chrom browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# headless option (창을 띄우지 않음) - 보안이 우회가능
chrome_options.add_argument("--headless")

# driver connection
goto_url = "https://www.amazon.com/Seagate-Expansion-Desktop-Drive-Black/dp/B07VS8QCXC/ref=sr_1_1?crid=1YXA3ADINFS8O&dib=eyJ2IjoiMSJ9.O-iz_OxFgbx8bLQuv31KFNq9EqEsv06BvQkuwEn6cNPNtFGUdYqwHmnbzkunELII3GzVPoGIDiQUnkTCGdDqjQly1Fhy8RbRdvxYRjrrcAG4n8hLu605tUVwzGp_Ft1N9Nz7RQqs26WYAQsuENh_GXyxzssO78dshrh_jodARrBN_Dp8LGOVPPKvhLVyFw7tui9ggRl03cAFSKPv2iVV-MXw-Z3-lIMBG3QXB21Khso.I3JpZThvqbKGyQYrEMFHxSSXuMTPDdCwL__aAMPv4Mo&dib_tag=se&keywords=portable%2Bhard%2Bdisk%2B8tb&qid=1719035880&sprefix=portablehard%2Bdisk%2B8tb%2Caps%2C221&sr=8-1&th=1"
driver = webdriver.Chrome(options=chrome_options)
driver.get(goto_url)

price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')

print(f"The price is {price_dollar.text}.{price_cents.text}")
# close just chrome tap
# driver.close()

# quit chrome browser
# driver.quit()

