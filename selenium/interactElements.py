from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open a website
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Find an element by name and interact with it
title = driver.title
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

time.sleep(5)
# Input text and submit
text_box.send_keys("Selenium")
submit_button.click()

time.sleep(5)
# Find another element and retrieve its text
message = driver.find_element(by=By.ID, value="message")
text = message.text

# Print the retrieved text
print(text)

# Close the browser
driver.quit() #[26, 27, 28]