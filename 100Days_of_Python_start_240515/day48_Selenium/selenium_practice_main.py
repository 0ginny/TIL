from selenium import webdriver


# to keep chrom browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# driver connection
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

# close just chrome tap
# driver.close()

# quit chrome browser
# driver.quit()