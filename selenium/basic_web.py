from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver
driver = webdriver.Chrome()   # or webdriver.Chrom(executable_path="path_to_chromedriver")

# Open a website
driver.get("https://www.qualcomm.com")

# Wait a bit for the page to load
time.sleep(10)

# Find an element (example: <a> tag) and click it
link = driver.find_element(By.TAG_NAME, "href")
link.click()

# Fil a form (example)
# input_box = driver.find_element(By.ID, "input-field-id")
# input_box.send_keys("Your Text")

# Close browser after a delay
time.sleep(10)
driver.quit()


