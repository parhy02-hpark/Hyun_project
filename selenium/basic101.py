from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#service = Service()
driver = webdriver.Chrome()
driver.get('https://www.dexcom.com')
print(driver.title)
time.sleep(5)
driver.quit()
